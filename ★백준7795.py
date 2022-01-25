import sys
input=sys.stdin.readline


t=int(input())
for i in range(t):
    sum=0
    N,M=map(int, input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    a=0
    b=0
    n=len(A)
    m=len(B)
    while a < n and b < m:
        if A[a] > B[b]:
            sum += m - b
            a += 1
        else:
            b += 1
        
    print(sum)