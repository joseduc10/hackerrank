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
        for j in xrange(i+1,n):
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


def sol2(n,arr):
    totalTriplets = 0
    arrMax = arr.max()
    seen = zeros(arrMax) > 0
    globalSeen = zeros(arrMax, int32)
    greater = zeros((n), int16)
    #g = [[] for i in xrange(n)]

    for i in xrange(n-2,-1,-1):
        #triplets = 0
        a = arr[i]
        seen[:] = False
        #print "iteration %s: %s" %(i,arr[i])
        for j in xrange(i+1, n):
            b = arr[j]
            #print a, b
            if a == b:
                greater[i] += greater[j]
                #g[i] += g[j]
                break
            if b > a and not seen[b-1]:
                if globalSeen[b-1] and globalSeen[a-1] \
                                        and globalSeen[b-1] > globalSeen[a-1]:
                    totalTriplets += greater[j] - greater[globalSeen[b-1]]
                    #print globalSeen
                    #print "Entered here"
                else:
                    totalTriplets += greater[j]
                    #print "entered there"
                    greater[i] += 1
                #g[i].append(j)
                #totalTriplets += greater[j]
                #triplets += greater[j]
                seen[b-1] = True
        if not globalSeen[a-1]:
            globalSeen[a-1] = i
        #print globalSeen
        #print "Total triplets from here: %s" %triplets
        #totalTriplets += triplets
    print totalTriplets
    #triplets = []
    #seen=[]
    #for i in xrange(n):
    #    a = g[i]
    #    if a not in seen:
    #        seen.append(a)
    #        for j in xrange(len(a)):
    #            b = g[a[j]]
    #            for k in xrange(len(b)):
    #                triplets.append((arr[i],arr[a[j]], arr[b[k]]))
    #print len(set(triplets))
    #for ind,i in enumerate(g):
    #    print arr[ind], ':', [arr[j] for j in i]
    #for i in triplets: print i

def main():
    #reading the input
    global comb, fact
    n = int(raw_input())
    arr = array([int(i) for i in raw_input().split()],int32)
    #initialization for sol1
    #comb, fact = zeros((n), int64), zeros((n), int64)
    #fact[0] = 1

    #sol1(n,arr)
    sol2(n,arr)

if __name__=='__main__':
    main()
