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
    #현재 구간과 이번 선분이 합쳐질 수 있다.
    if r<List[i][0]:
        #결과에 더한다.
        result+=r-l;
        #현재 구간을 이번 선분으로 초기화한다.
        l=List[i][0]; r=List[i][1]
    #합쳐진다. 현재 구간의 r을 늘릴 수 있다면 늘린다.
    else: r=max(r,List[i][1])

result+=r-l;
print(result)