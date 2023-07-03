Seat=[0 for _ in range(101)]
N=int(input())
List=list(map(int,input().split()))
ans=0
for i in range(N):
    if Seat[List[i]]==1: ans+=1
    else: Seat[List[i]]=1
print(ans)