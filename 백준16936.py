import sys
input=sys.stdin.readline

N=int(input())
List_=list(map(int,input().split()))
List=List_.copy()
modList=[0 for _ in range(N)]
MAX=0; MAXINDEX=0
for i in range(N):
    while True:
        if List[i]%3==0: List[i]//=3; modList[i]+=1
        else: break
    if modList[i]>MAX or (modList[i]==MAX and List_[i]<List_[MAXINDEX]): MAX=modList[i]; MAXINDEX=i
ans=[]
first=List_[MAXINDEX]
ans.append(first)
num=1
for i in range(N):
    if first*2 in List_:
        x=List_.index(first*2)
        first=List_[x]
        ans.append(first)
        num+=1
        if num==N: break;
        continue
    if first%3==0 and first//3 in List_:
        x=List_.index(first//3)
        first=List_[x]
        ans.append(first)
        num+=1
        if num==N: break;
        continue

print(*ans)