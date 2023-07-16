N=int(input())
List=[]
for _ in range(N):
    List.append(int(input()))
List=sorted(List)
List+=[0]
ans=0
for i in range(N,-1,-3):
    ans+=List[i]
print(sum(List)-ans)