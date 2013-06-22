#!/usr/bin/python
import re

def main():
    n = int(raw_input())
    strings = [raw_input() for i in range(n)]

    start,end = re.compile(r'^hackerrank'), re.compile(r'hackerrank$')

    for s in strings:
        matchStart, matchEnd = start.search(s), end.search(s)
        if matchStart and matchEnd: print 0
        elif matchStart: print 1
        elif matchEnd: print 2
        else: print -1

if __name__=="__main__":
    main()

