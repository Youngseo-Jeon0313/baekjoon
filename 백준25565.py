import heapq
from collections import deque
N,M,K=map(int,input().split())
Board=[list(map(int,input().split())) for _ in range(N)]

minheap=[]
maxheap=[]
ansheap=[]
q=deque([])
heapq.heapify(minheap)
heapq.heapify(maxheap)
heapq.heapify(ansheap)
for i in range(N):
    for j in range(M):
        if Board[i][j]==1:
            heapq.heappush(minheap,[i,j])
            heapq.heappush(maxheap,[-i,j])
            q.append([i+1,j+1])
if len(minheap)==K: 
    for i in q:
        heapq.heappush(ansheap,i)

elif len(minheap)==2*K: print(0); exit();
else:
    #print(-maxheap[0][0]-minheap[0][0])
    if -maxheap[0][0]-minheap[0][0]==K-1: 
        for i in range(N):
            for j in range(M):
                check1=0; check2=0
                if Board[i][j]:
                    if (i-1>=0 and Board[i-1][j]) or (i+1<N and Board[i+1][j]):
                        check1=1
                    if (j-1>=0 and Board[i][j-1]) or (j+1<M and Board[i][j+1]):
                        check2=1
                if check1 and check2: 
                    print(1); print(i+1,j+1); exit();
    else:
        for k in range(K-(2*K-len(maxheap)),K):
            # print('저기야')
            heapq.heappush(ansheap,[q[k][0],q[k][1]])

print(len(ansheap))
if len(ansheap):
    while len(ansheap):
        x=heapq.heappop(ansheap)
        print(*x)



