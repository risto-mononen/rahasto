#! /usr/bin/env python

import time
import os
import urllib
import tocsv
from cStringIO import StringIO
import sys
from subprocess import call

fund_type = dict(
    Hedge=4,
    Bond=3,
    Unclassified=9,
    Stock=1,
    Balanced=2)

def download(typeid, filename):
    template = 'http://www.kauppalehti.fi/5/i/porssi/rahastot/index.jsp?fcomid=&type={typeid}&class=&N%E4yt%E4.x=29&N%E4yt%E4.y=6&N%E4yt%E4=N%E4yt%E4'
    url = template.format(**locals())
    f = urllib.urlopen(url)
    ret = f.read()
    f.close()
    return ret

def store(data, filename):
    with open(filename, 'w') as outfile:
        outfile.write(data)

def download_all(funds, import_script):
    TODAY = time.strftime('%Y%m%d')
    ret = 0
    for name, typeid in funds.items():
        fname = '{TODAY}-{name}'.format(**locals())
        print >> sys.stderr, 'download ', fname
        html_page = download(typeid, fname + '.html')
        store(html_page, fname + '.html')
        print >> sys.stderr, 'parse csv ', name
        ret, csvfile = parse(html_page, name)
        call([import_script, csvfile])
    return ret

def parse(html, name):
    stdout = sys.stdout
    sys.stdout = StringIO()
    ret = tocsv.parse_string(html)
    csvfile = name + '.csv'
    with open(csvfile, 'w') as out:
        out.write(sys.stdout.getvalue())
    sys.stdout.close()
    sys.stdout = stdout
    return ret, csvfile


def main(argv=None):
    if argv is None:
        argv = sys.argv
    ret = 0
    pathname = os.path.dirname(sys.argv[0])        
    abspath = os.path.abspath(pathname)
    full_path = os.path.join(abspath, 'import.sh')
    if len(argv) < 2:
        ret = download_all(fund_type, full_path)
    else:
        for arg in argv:
            with open(arg) as f:
                ret += download_all(fund_type, full_path)
    return ret


if __name__ == "__main__":
    sys.exit(main())
