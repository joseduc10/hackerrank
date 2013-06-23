#!/usr/bin/python
import re

def main():
    n = int(raw_input())
    requests = [raw_input() for i in xrange(n)]

    languages ='C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:' + \
       'BASH:SCALA:ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:' + \
       'OCAML:R:PASCAL:SBCL:DART:GROOVY:OBJECTIVEC'
    languages = languages.replace(':','|')

    regex = re.compile('^[0-9]{1,5} (' + languages + ')$')
    
    for r in requests:
        if regex.search(r):
            print 'VALID'
        else:
            print 'INVALID'

if __name__=='__main__':
    main()
