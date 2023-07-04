T=int(input())
for _ in range(T):
    P,M=map(int,input().split())
    ans=0
    seat=[0 for _ in range(M)]
    for _ in range(P):
        a=int(input())
        if seat[a-1]: ans+=1
        seat[a-1]=1
    print(ans)
