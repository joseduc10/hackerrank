#!/usr/bin/python
from numpy import *

def sol1(n,k,p):
    '''
        First (naive) idea. opt[i][j] represents the optimal solution 
        (i.e. set of at most k billboards with maximum profit) of the 
        subproblem that uses only the billboards from i to j.
        First, if there are at most k billboards, simply use all the billboards.
        Otherwise, the optimal solution either includes one of the end points 
        but not the other, OR it includes both endpoints but not some billboards 
        in between. More formally, let p_i be the profit associated with billboard i.
        Then,

        opt[i][j] = \sum_{l=i}^j p_l  ; if j-i+1 <= k
        opt[i][j] = \max{opt[i+1][j], opt[i][j-1], max_{i<l<j}{opt[i][l-1] + opt[l+1][j]}}

        Implementation uses an nxn matrix (only the upper diagonal is used). Matrix is 
        filled diagonally, and the answer is given by opt[0][n-1]

        Space Complexity: O(n^2)
        Time Complexity: O(n^3)
    '''
    #initialization
    opt = [[0 for i in xrange(n)] for j in xrange(n)]
    for i in xrange(n):
        opt[i][i] = p[i]

    #fill the matrix
    for l in xrange(1,n):
        for i in xrange(n-l):
            j = i+l
            if j-i+1 <= k:
                opt[i][j] = sum(p[i:j+1])
            else:
                opt[i][j] = max(opt[i+1][j],opt[i][j-1], 
                            max([0] + [opt[i][m-1]+opt[m+1][j] for m in xrange(i+1,j)]))
    print opt[0][n-1]


def sol2(n,k,p):
    '''
        Second idea. Huge improvement in space and time complexity.
        This time opt[i] represents the optimal solution of the subproblem 
        that uses billboards 0 to i-1 (or 1 to i if we use 1-indexed lists).
        Again, if i is at most k, the optimal soluton simply uses all the 
        billboards. Otherwise, there are a couple of cases to consider. 
        
        1) We don't use the ith billboard
          - In this case, then, we preserve the optimal solution of using the first
            i-1 billboards
        2) We use the ith billboard
          - Here we have to consider how the ith billboard interacts with the first 
            i-1. By adding billboard i, we could improve the solution as follows: 
            It may be the case that combining billboard i with the last k-1 billboards 
            from 1 to i-1 improves the solution. So we have to try the effect of using 
            billboards i and i-1, and then skipping i-2, OR using i, i-1, i-2, and then 
            skipping i-3, all the way up to using i,i-1,...,i-k+1, and then skipping i-k.
            Formally,

            opt[i] = \sum_{j=1}^i p_j   ; if i <= k
            opt[i] = max_{i-k+1 <= j <= i} \sum_{l=j}^i p_l + opt[l-2]

            Space Complexity: O(n)
            Time Complexity: O(kn) = O(n^2), since k <= n (k is usually small compared to n)
    '''
    opt = [0 for i in xrange(n)]
    opt[0] = p[0]

    for i in xrange(1,n):
        if i <= k-1:
            opt[i] = p[i] + opt[i-1]
        else:
            x = 0
            for j in xrange(k):
                s = 0
                for l in xrange(i-j,i+1):
                    s += p[l]
                s += opt[i-j-2]
                if x < s: x = s
            opt[i] = max(opt[i-1], x)
    print opt[n-1]


def sol3(n,k,p):
    '''
        Re-implementation of sol2 optimized using numpy arrays.
        Also, this version has an extra array (mem for memoize) 
        to avoid re-calculating the sum of adjacent billboards 
        every single time.
        This version passes all test cases taking no longer than
        15 seconds in each input
    '''
    opt = zeros((n+1), int64)
    mem = array(p, int64)

    #special case. Instance of the Independent Set in Path Graph problem
    if k == 1:
        for i in xrange(2,n+1):
            opt[i] = max(p[i]+opt[i-2], opt[i-2])
        print opt[n]
        return

    for i in xrange(1,k+1):
        opt[i] = p[i]+opt[i-1]

    for i in xrange(2,k):
        mem[k-i+1] += mem[k-i+2]
    mem[2:k] += opt[0:k-2]

    for i in xrange(k+1,n+1):
        mem[i-k+1:i] += p[i]
        mem[i-1] += opt[i-3]
        opt[i] = max(opt[i-1], p[i]+opt[i-2], (mem[i-k+1:i]).max())
    print opt[n]


def main():
    #reading the input
    n,k = [int(i) for i in raw_input().split()]
    p = zeros((n+1),int64)
    for i in xrange(1,n+1):
        p[i] = int(raw_input())

    sol3(n,k,p)

if __name__=='__main__':
    main()
