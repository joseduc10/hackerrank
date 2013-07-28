#!/usr/bin/python

def sol1(M,D,n):
    '''
        First idea: Check if i and i-k are part of arr by creating 
        an array 'exists' of length max(arr). In this array, the ith entry 
        indicates if the number i is in arr (True) or not (False).
        Then, simply multiply the ith and (i-k)th entry in 'exists'.
        This product will be either 1 (which means that we found a pair 
        whose difference is k) or 0 (either i or i-k are missing).

        Space complexity: O(max(arr)) =  O(2^31-1)
        Time complexity: O(n + max(arr))

        Which makes this algorithm pseudo-polynomial and very slow for
        high values of max(arr)
    '''
    T = [M[i] - D[i] for i in xrange(n)]
    complete = [False for i in xrange(n)]
    maxT = 0
    countComplete = 0
    while countComplete < n:
        #print T
        latest = -1000000; latestJob = None
        for i in xrange(len(T)):
            if complete[i]: continue
            if T[i] > latest:
                latest = T[i]; latestJob = i
            maxT = max(maxT, T[i])
            T[i] += 1
        T[latestJob] -= 1
        M[latestJob] -= 1
        #print "M[%s] = %s" %(latestJob, M[latestJob])
        
        if not M[latestJob]:
            complete[latestJob] = True
            countComplete += 1
    return maxT

def sol2(M,D,n):
    '''
        Second idea: Same intuition as before. For each number i in arr, 
        we want to check if i+k is in arr as well.
        In this case, create an array 'shifted' of length n. Let x be the 
        ith entry in arr; then, the ith entry in 'shifted' is x+k.
        We treat arr and shifted as sets, and find the interception, which
        implicitely tells us if both x and x+k are in arr.

        Space complexity: O(n)
        Time complexity: O(n)

        This version passes the hardest test case in 0.22 seconds.
    '''
    #sortedJobs = sorted(jobs)
    opt = [0 for i in xrange(n+1)]
    maxd, totalm = 0, 0
    for i in xrange(1,n+1):
        #print "iteration", i
        totalm += M[i-1]
        if D[i-1] <= maxd:
            opt[i] = opt[i-1] + M[i-1]
        else:
            opt[i] = max(opt[i-1], totalm - D[i-1])
        #print "opt[i]: %s" %opt[i]
        maxd = max(maxd, D[i-1])
        #print "D[i]: %s, M[i]: %s" %(D[i-1],M[i-1])
        #print "maxd: %s, totalm: %s" %(maxd, totalm)
        #print "------------------"
    return opt

def main():
    #reading the input
    n = int(raw_input())
    M, D = [],[]
    jobs = []
    for i in xrange(n):
        d_j, m_j = [int(i) for i in raw_input().split()]
        D.append(d_j)
        M.append(m_j)
        jobs.append((d_j, m_j))

    #for i in xrange(n):
    #    print sol1(M[:i+1],D[:i+1],i+1)

    opt = sol2(M,D,n)
    for i in xrange(1,n+1):
        print opt[i]

if __name__=='__main__':
    main()


