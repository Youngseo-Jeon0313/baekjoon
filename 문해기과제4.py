
from collections import deque

N,M=map(int,input().split()) 
# 가로로 N개, 세로로 M개 존재한다.
# 가장 왼쪽 1,1 가장 오른쪽 아래 M,N -> 그냥 0,0 M-1,N-1로 두고 풀자

List=[]
DP=[[0 for _ in range(N)] for _ in range(M)]

for _ in range(M):
    List.append(list(map(int,input().split())))

#init
DP[0][0]=List[0][0]

#BFS + DP
deq=deque([[0,0]])
while deq:
    x,y=deq.popleft()
    if x>M-1 and y>N-1: continue
    if x%2:
        for i,j in [[0,1],[1,1]]:
            if x+i<M and y+j<N:
                DP[x+i][y+j]=max(DP[x+i][y+j],DP[x][y]+List[x+i][y+j])
                deq.append([x+i,y+j])
    else:
        for i,j in [[1,0],[0,1]]:
            if x+i<M and y+j<N:
                DP[x+i][y+j]=max(DP[x+i][y+j],DP[x][y]+List[x+i][y+j])
                deq.append([x+i,y+j])
    # print(deq)
print(DP)
print(DP[M-1][N-1])


