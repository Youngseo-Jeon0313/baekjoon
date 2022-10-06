import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    n=int(input())
    L=list(map(int,input().split()))
    L.sort()
    ans=float('inf')
    for i in range(1,n-1):
        ans=min(ans,abs(L[i]-L[i-1])+abs(L[i]-L[i+1]))
    print(ans)