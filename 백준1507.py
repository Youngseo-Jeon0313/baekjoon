import copy

N=int(input())
List=[]
for _ in range(N):
    List.append(list(map(int,input().split())))

newList=copy.deepcopy(List)

flag=True
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i==j or j==k or i==k: continue
            if List[i][k]+List[k][j]==List[i][j]:
            # print(i,j,k)
                newList[i][j]=0; newList[j][i]=0
            elif List[i][k]+List[k][j]<List[i][j]:
                flag=False
ans=0
# print(newList)
for i in range(N):
    ans+=sum(newList[i])

if flag:
    print(ans//2)
else:
    print(-1)