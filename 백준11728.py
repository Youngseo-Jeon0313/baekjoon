import sys
input=sys.stdin.readline

N,M=map(int,input().split())
#시간 복잡도 1000000*2
newList=[]
AList=list(map(int,input().split()))
BList=list(map(int,input().split()))

Apoint=0; Bpoint=0;
while Apoint<N and Bpoint<M:
    if AList[Apoint]<BList[Bpoint]:
        newList.append(AList[Apoint])
        Apoint+=1
    else:
        newList.append(BList[Bpoint])
        Bpoint+=1
# print(Apoint,Bpoint)

if Apoint<N:
    for i in range(Apoint,N):
        newList.append(AList[i])
if Bpoint<M:
    for i in range(Bpoint,M):
        newList.append(BList[i])
print(*newList)


