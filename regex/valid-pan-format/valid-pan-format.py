#!/usr/bin/python
import re

def main():
    n = int(raw_input())
    pans = [raw_input() for i in xrange(n)]
    regex = re.compile('[A-Z]{5}[0-9]{4}[A-Z]')
    
    for p in pans:
        if regex.search(p):
            print 'YES'
        else:
            print 'NO'

if __name__=='__main__':
    main()
