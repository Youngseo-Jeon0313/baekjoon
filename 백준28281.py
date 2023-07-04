ans=float('inf')
N,X=map(int,input().split())
List=list(map(int,input().split()))
for i in range(N-1):
    ans=min(ans,X*(List[i]+List[i+1]))
print(ans)