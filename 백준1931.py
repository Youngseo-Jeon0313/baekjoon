N=int(input())

List=[]
for _ in range(N):
    x,y=map(int,input().split())
    List.append((x,y))
List=sorted(List,key=lambda x:[x[1],x[0]])
ans=0
start=0
for i,j in List:
    if i>=start:
        ans+=1; start=j

print(ans)