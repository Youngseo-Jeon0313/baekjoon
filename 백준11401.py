import sys
input=sys.stdin.readline
MOD=1000000007

def factorial(N):
    n=1
    for i in range(2,N+1):
        n = (n*i)%MOD
    return n

def fpow(c,n):
    if n==0: return 1
    if n==1: return c
    else: 
        x=fpow(c,n//2)
        if n%2:return x*x*c%MOD
        else: return x*x%MOD
N,K=map(int,input().split())
A=factorial(N)
B=factorial(N-K)*factorial(K)%MOD

print(A*fpow(B,MOD-2)%MOD)