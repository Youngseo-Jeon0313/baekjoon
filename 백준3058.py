t=int(input())
for _ in range(t):
    L=list(map(int,input().split()))
    ans=0; MIN=float('inf')
    for i in L:
        if i%2==0: ans+=i; MIN=min(MIN,i)
    print(ans,MIN)