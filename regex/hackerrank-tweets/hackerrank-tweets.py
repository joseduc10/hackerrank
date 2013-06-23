#!/usr/bin/python
import re

def main():
    n = int(raw_input())
    strings = [raw_input() for i in xrange(n)]
    regex = re.compile('hackerrank', re.IGNORECASE)

    print len([regex.search(s) for s in strings if regex.search(s)])

if __name__=="__main__":
    main()
