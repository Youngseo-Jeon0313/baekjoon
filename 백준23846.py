import sys
input=sys.stdin.readline


def fac(n) :
    ans = 1
    if n == 0 :
        return 1
    else :
        for i in range(1, n + 1) :
            ans = ans * i 
            ans%= int(1e9+7)
        return ans
        
def com(n, r) :
    return fac(n) / fac(r) / fac(n - r)


N,K=map(int,input().split())
ans=0
for i in range(K):
    ans+=com(N,i)


print(format((1/3)**N*ans,'.1000f'))


