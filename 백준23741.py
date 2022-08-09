import sys
input=sys.stdin.readline
from collections import deque

N,M,X,Y=map(int,input().split())
List=[[] for _ in range(N+1)]
visit=[[0 for _ in range(Y+1)] for _ in range(N+1)] #pos,visit를 방문표시할 visit함수
for _ in range(M):
  x,y=map(int,input().split())
  List[x-1].append(y-1)
  List[y-1].append(x-1)

deq=deque([])
deq.append([X-1,0])
visit[X-1][0]=1
ans=[]
while deq:
  pos,depth=deq.popleft()
  if depth==Y and pos+1 not in ans: ans.append(pos+1) #%2==Y%2
  if depth<Y:
      for i in List[pos]:
          if not visit[i][depth+1]:
            deq.append([i,depth+1])
            visit[i][depth+1]=1
ans.sort()
if len(ans)==0: print(-1)
else: print(*ans)
