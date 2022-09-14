import sys
input=sys.stdin.readline

T=int(input())

for _ in range(T):
    N,M,K=map(int,input().split())
    s=list(map(int,input().split()))
    check=[0 for _ in range(N)]
    check[0]=s[0]
    ans=0
    for i in range(1,N):
        check[i]=check[i-1]+s[i]
    for i in range(M-1,N):
        if i==M-1:
            if check[i]<K:ans+=1
        else:
            if check[i]-check[i-M]<K: ans+=1
    if M>1 and N!=M:
        for i in range(1,M):
            if check[N-1]-check[N-1-i]+check[M-i-1]<K:ans+=1
    print(ans)
