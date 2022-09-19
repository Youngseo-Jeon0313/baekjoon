import sys
input=sys.stdin.readline

N,M,Q=map(int,input().split())
List=list(map(int,input().split()))
SubList=List.copy()
for i in range(1,N):
    SubList[i]+=SubList[i-1]

water=[0 for _ in range(N)]

for i in range(N):
    mod=List[i]//M
    res=List[i]%M
    # print(mod,res)
    for j in range(mod):
        if i+j>N-1: break;
        water[i+j]+=M
    if res and i+mod+1<=N-1:
        water[i+mod]+=res
    # print(water)

watersum=water.copy()
for i in range(1,N):
    watersum[i]+=watersum[i-1]


# print('자자',SubList)
# print('워워',watersum)
# print('워터다',water)
for _ in range(Q):
    x,y=map(int,input().split())
    
    if x==2:
        if y==1: print(0)
        else:
            print(water[y-2])
    else:
        if y==1:
            print(SubList[0])
        else:
            print(SubList[y-1]-watersum[y-2])
