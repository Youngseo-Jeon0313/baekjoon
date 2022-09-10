import sys
input=sys.stdin.readline
MOD=1000000007

fact=[1]*4000001
for i in range(2,4000001):
    fact[i]=fact[i-1]*i
    fact[i]%=MOD
def fpow(c,n):
    if n==0: return 1
    if n==1: return c
    else: 
        x=fpow(c,n//2)
        if n%2:return x*x*c%MOD
        else: return x*x%MOD
M=int(input())
for _ in range(M):
    N,K=map(int,input().split())
    A=fact[N]
    B=fact[N-K]*fact[K]%MOD

    print(A*fpow(B,MOD-2)%MOD)









