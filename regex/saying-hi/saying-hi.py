#!/usr/bin/python
import re

def main():
    n = int(raw_input())
    strings = [raw_input() for i in xrange(n)]
    regex = re.compile('^hi [^d]', re.IGNORECASE)

    for s in strings:
        if regex.search(s):
            print s

if __name__=="__main__":
    main()
