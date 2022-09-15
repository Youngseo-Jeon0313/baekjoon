import sys
input=sys.stdin.readline

from collections import deque

N,M=map(int,input().split())
ans=0
q=deque([])
ansq=deque([])
Dict={i:0 for i in range(1,N+1)}

for _ in range(N):
    x,y=map(int,input().split())
    q.append([x,y])
    Dict[x]+=1

for i in range(M,0,-1):
    index=0
    while Dict[i]:#q를 한 바퀴돌면서 파악
        x,y=q.popleft()
        #print(ansq, ans)
        if x==i:
            Dict[x]-=1
            tempq=deque([])
            if len(ansq) and ansq[-1][0]==x and ansq[-1][1]<y:
                while len(ansq) and ansq[-1][0]==x and ansq[-1][1]<y:
                    tempx_,tempy_=ansq.pop();
                    ans+=tempy_
                    tempq.append([tempx_,tempy_]);
                ansq.append([x,y]); ans+=y
                while tempq:
                    tempx,tempy=tempq.pop();
                    ans+=tempy
                    ansq.append([tempx,tempy])
            else:
                ans+=y
                ansq.append([x,y])
        else:
            ans+=y
            q.append([x,y])
    # print(ansq)
print(ans)
