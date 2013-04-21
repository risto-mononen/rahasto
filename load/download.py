#! /usr/bin/env python

import time
import os
import urllib
import tocsv
from cStringIO import StringIO
import sys

fund_type = dict(
    Hedgerahastot=4,
    Korkorahastot=3,
    Luokittelemattomat=9,
    Osakerahastot=1,
    Yhdistelmarahastot=2)

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

def download_all(funds):
    TODAY = time.strftime('%Y%m%d')
    ret = 0
    for name, typeid in funds.items():
        fname = '{TODAY}-{name}'.format(**locals())
        print >> sys.stderr, 'download ', fname
        html_page = download(typeid, fname + '.html')
        store(html_page, fname + '.html')
        print >> sys.stderr, 'parse csv ', name
        stdout = sys.stdout
        sys.stdout = csv = StringIO()
        ret += tocsv.parse_string(html_page)
        sys.stdout = stdout
        with open(name + '.csv', 'w') as out:
            out.write(csv.getvalue())
        csv.close()
        # TODO: mysqlimport name.csv
    return ret


def main(argv=None):
    if argv is None:
        argv = sys.argv
    ret = 0
    if len(argv) < 2:
        ret = download_all(fund_type)
    else:
        for arg in argv:
            with open(arg) as f:
                ret += download_all(fund_type)
    return ret


if __name__ == "__main__":
    sys.exit(main())
