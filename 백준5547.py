'''
벌꿀집으로 볼 수 있어야 함

많은 조건분기
'''
from collections import deque
W,H=map(int,input().split())
house=[]
for _ in range(H):
    house.append(list(map(int,input().split())))

DP=[[0 for _ in range(W)] for _ in range(H)]

#init
DP[0][0]=house[0][0]

#BFS + DP
deq=deque([[0,0]])
while deq:
    x,y=deq.popleft()
    if x>W-1 and y>H-1: continue
    if x%2:
        for i,j in [[0,1],[1,1]]:
            if x+i<W and y+j<H:
                DP[x+i][y+j]=max(DP[x+i][y+j],DP[x][y]+house[x+i][y+j])
                deq.append([x+i,y+j])
    else:
        for i,j in [[1,0],[0,1]]:
            if x+i<W and y+j<H:
                DP[x+i][y+j]=max(DP[x+i][y+j],DP[x][y]+house[x+i][y+j])
                deq.append([x+i,y+j])
    # print(deq)


