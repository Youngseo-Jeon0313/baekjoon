T=int(input())
for _ in range(T):
    n=int(input())
    List=list(map(int,input().split()))
    List=sorted(List)
    ans=0
    for i in range(1,n):
        ans+=List[i]-List[i-1]
    print(2*ans)