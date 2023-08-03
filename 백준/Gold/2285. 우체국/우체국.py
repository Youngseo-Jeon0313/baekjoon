N=int(input())
List=[]
total=0
for _ in range(N):
    a,b=map(int,input().split())
    List.append((a,b))
    total+=b
List=sorted(List, key = lambda x :x[0])
target=total/2
SUM=0
ans=0
for i in List:
    SUM+=i[1]
    if SUM>=target: 
        # print(SUM, target)
        ans=i[0]; break;

print(ans)