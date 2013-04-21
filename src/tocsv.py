#! /usr/bin/env python

import sys
from HTMLParser import HTMLParser, HTMLParseError

stack = list()

def skip(*args): pass

class FundParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        #super(FundParser, self).__init__()
        self.handle_starttag, self.handle_endtag, self.handle_data = self.preamble, skip, skip
        self.inpre = self.handle_starttag == self.preamble
        self.postfix = dict(tr='\n', td=',')
        self.buf = list()

    def preamble(self, tag, attrs):
        assert self.inpre
        assert self.handle_starttag == self.preamble
        if tag == 'div' and ('class', 'module') in attrs:
            stack.append((tag, attrs))
            self.handle_starttag, self.handle_endtag = self.inmodule, self.end
            predone = True

    def end(self, tag):
        if self.postfix.has_key(tag):
            print self.postfix[tag],
        try:
            start = stack.pop()
        except IndexError:      # End of well formed input, ignore the rest
            self.handle_starttag, self.handle_endtag, self.handle_data = skip, skip, skip
            return
        if tag != start[0]:
            raise TagMismatch(start, tag)

    def inmodule(self, tag, attrs):
        if tag != 'img':        # Missing end tags
            stack.append((tag, attrs))
        if tag == 'tr':
            self.handle_data = self.data

    def data(self, data):
        print data.strip(),

class TagMismatch(SyntaxError): pass

def parse_string(s):
    parser = FundParser()
    try:
        parser.feed(s)
    except HTMLParseError:
        return 0
    return 0

def parse_file(f):
    return parse_string(f.read())

def main(argv=None):
    if argv is None:
        argv = sys.argv
    if len(argv) < 2:
        return parse_file(sys.stdin)
    ret = 0
    for arg in argv:
        with open(arg) as f:
            ret += parse_file(f)
    return ret

if __name__ == "__main__":
    sys.exit(main())
