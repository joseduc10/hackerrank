#!/usr/bin/python

def sol1(n,k,p):
    #initialization
    opt = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        opt[i][i] = p[i]

    #fill the matrix
    for l in range(1,n):
        for i in range(n-l):
            j = i+l
            if j-i+1 <= k:
                opt[i][j] = sum(p[i:j+1])
            else:
                opt[i][j] = max(opt[i+1][j],opt[i][j-1], 
                            max([0] + [opt[i][m-1]+opt[m+1][j] for m in range(i+1,j)]))
    print opt[0][n-1]


def sol2(n,k,p):
    opt = [0 for i in range(n)]
    opt[0] = p[0]

    for i in range(1,n):
        #print "i=",i
        if i <= k-1:
            opt[i] = p[i] + opt[i-1]
        else:
            x = 0
            for j in range(k):
                s = 0
                for l in range(i-j,i+1):
                    s += p[l]
                s += opt[i-j-2]
                if x < s: x = s
            opt[i] = max(opt[i-1], x)
            #opt[i] = max(opt[i-1], max([sum([p[l] for l in range(i-j,i+1)]) + opt[i-j-2] \
            #                           for j in range(k)]))
            #print [sum([p[l] for l in range(i-j,i+1)]) + opt[i-j-2] for j in range(k)]
    print opt[n-1]

def sol3(n,k,p):
    opt = [0 for i in range(n)]
    opt[0] = p[0]
    mem = p[:]

    for i in range(1,k-1):
        mem[k-i-1] += mem[k-i]

    #print p
    #print mem
    for i in range(1,k):
        opt[i] = p[i]+opt[i-1]

    for i in range(k,n):
        #print "i=",i
        x = p[i] + opt[i-2]
        for j in range(1,k):
            mem[i-j] += p[i]
            s = mem[i-j] + opt[i-j-2]
            if x < s: x = s
        if opt[i-1] > x:
            opt[i] = opt[i-1]
        else:
            opt[i] = x
    print opt[n-1]


def main():
    #getting the input
    n,k = [int(i) for i in raw_input().split()]
    p = []
    for i in range(n):
        p.append(int(raw_input()))

    #sol1(n,k,p)
    #sol2(n,k,p)
    sol3(n,k,p)

if __name__=='__main__':
    main()
