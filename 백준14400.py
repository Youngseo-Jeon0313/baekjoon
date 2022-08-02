import sys
input=sys.stdin.readline
N=int(input())
List=[]
for _ in range(N):
    x,y=map(int,input().split())
    List.append([x,y])
List_x=sorted(List,key=lambda x:x[0])
List_y=sorted(List,key=lambda x:x[1])
ans_x=List_x[N//2][0]
ans_y=List_y[N//2][1]

ans=0
for i in range(N):
    ans+=abs(List[i][0]-ans_x)
    ans+=abs(List[i][1]-ans_y)
print(ans)