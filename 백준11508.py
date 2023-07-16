
N=int(input())
List=[]
for _ in range(N):
    List.append(int(input()))
List=sorted(List)
ans=sum(List)
a=len(List)//3
for i in range(a):
    ans-=List[i]
print(ans)

