import sys
input=sys.stdin.readline


N=int(input())
List=[]

for _ in range(N):
    x,y=map(int,input().split())
    List.append([x,y])

List.sort()
result=0; l=List[0][0]; r=List[0][1]
#[l,r]: 현재 합치고 있는 구간
for i in range(N):
    #새로운 구간에 들어오게 되었을 때 지금까지의 것을 더하는 것.
    if r<List[i][0]:
        print('아',r)
        #결과에 더한다.
        result+=r-l;
        #현재 구간을 이번 선분으로 초기화한다.
        l=List[i][0]; r=List[i][1]
    #구간이 협친다. r을 최대한으로 늘린다.
    else: 
        print(r)
        r=max(r,List[i][1])

result+=r-l;
print(result)