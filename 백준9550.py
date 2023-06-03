T=int(input())
for _ in range(T):
    N,K=map(int,input().split())
    List=list(map(int,input().split()))
    ans=0
    for i in List: ans+=i//K
    print(ans)