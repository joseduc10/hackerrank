#!/usr/bin/python
import re

def main():
    n = int(raw_input())
    strings = [raw_input() for i in xrange(n)]
    t = int(raw_input())
    words = [raw_input() for i in xrange(t)]
    counts = [0 for i in range(t)]

    regexs = [re.compile(i[:-2] + '[sz]e') for i in words]

    for s in strings:
        for i, regex in enumerate(regexs):
            counts[i] += len(regex.findall(s))
    for i in counts:
        print i

if __name__=="__main__":
    main()
