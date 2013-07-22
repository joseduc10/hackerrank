#!/usr/bin/python

def sol1(n,k,arr):
    '''
        First idea: Check if i and i-k are part of arr by creating 
        an array 'exists' of length max(arr). In this array, the ith entry 
        indicates if the number i is in arr (True) or not (False).
        Then, simply multiply the ith and (i-k)th entry in 'exists'.
        This product will be either 1 (which means that we found a pair 
        whose difference is k) or 0 (either i or i-k are missing).

        Space complexity: O(max(arr)) =  O(2^31-1)
        Time complexity: O(n + max(arr))

        This algorithm is very slow for high values of max(arr). Along the same
        lines, it depends on the value of the input, rather than the size, so
        it's not a very satisfactory solution.
    '''
    exists = [False]
    for i in xrange(max(arr)):
        exists.append(i+1 in arr)
    minuend = exists[k+1:]
    subtrahend = exists[1:-k]
    return sum([minuend[i]*subtrahend[i] for i in xrange(len(minuend))])

def sol2(n,k,arr):
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
    shifted = [i+k for i in arr]
    return len(set(arr).intersection(set(shifted)))
    

def main():
    #reading the input
    n,k = [int(i) for i in raw_input().split()]
    arr = [int(i) for i in raw_input().split()]

    print sol2(n,k,arr)

if __name__=='__main__':
    main()
