#!/usr/bin/python
from numpy import *

comb = None
fact = None

def combination(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    if comb[n-1] == 0:
        comb[n-1] = factorial(n)/(2 * factorial(n-2))    
    return comb[n-1]
    
def factorial(n):
    if fact[n-1] == 0:
        lastSeen = where(fact > 0)[0][-1]
    for i in xrange(lastSeen+1,n):
        fact[i] = (i+1)*fact[i-1]
    return fact[n-1]

def sol1(n,arr):
    '''
    Re-implementation of sol2 optimized using numpy arrays.
    Also, this version has an extra array (mem for memoize) 
    to avoid re-calculating the sum of adjacent billboards 
    every single time.
    This version passes all test cases taking no longer than
    15 seconds in each input
    '''
    greater = zeros((n), int32)
    triplets = zeros((n), int32)
    seen = zeros(arr.max()) > 0
    #print arr
    for i in xrange(n-2,-1,-1):
        for j in xrange(i,n):
            if arr[i] < arr[j]:
                greater[i] = 1 + greater[j]
                break
        triplets[i] = combination(greater[i])
    #print greater
    #print triplets
    total = triplets[0]
    seen[arr[0]-1] = True
    for i in xrange(1,n):
        #print seen
        ind = arr[i]-1
        if not seen[ind]:
            total += triplets[i]
            seen[ind] = True
    print total

def main():
    #reading the input
    global comb, fact
    n = int(raw_input())
    arr = array([int(i) for i in raw_input().split()],int32)
    comb, fact = zeros((n), int64), zeros((n), int64)
    fact[0] = 1

    sol1(n,arr)

if __name__=='__main__':
main()
