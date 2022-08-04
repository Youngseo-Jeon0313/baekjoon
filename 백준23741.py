import sys
input=sys.stdin.readline
from collections import deque

N,M,X,Y=map(int,input().split())
List=[[] for _ in range(N+1)] #뭐가 뭐랑 연결되어있는지 체크
for _ in range(M):
    x,y=map(int,input().split())
    List[x].append(y)
    List[y].append(x)
ans=[]
'''
인자는 이렇게 한다.
-depth
-현재 정점의 위치
-그걸 담는 arr
'''

deque=([])



if len(ans)>0:
    print(list(set(ans)))
else:
    print(-1)