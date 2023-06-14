'''
벌꿀집으로 볼 수 있어야 함
상하좌우에 모두 0을 채워넣기
'''
from collections import deque
W,H=map(int,input().split())
house=[[0 for _ in range(W+2)]]
for _ in range(H):
    house.append([0]+list(map(int,input().split()))+[0])
house.append([0 for _ in range(W+2)])
#init
ans=0
check=[[0 for _ in range(W+2)] for _ in range(H+2)]

def dfs(a,b):
    res = 0
    #BFS 
    deq=deque([[a,b]])
    while deq:
        y,x=deq.popleft()
        check[y][x]=1 #방문 체크
        # print(y,x)
        if y%2:
            for i,j in [[-1,0],[1,0],[0,1],[1,1],[0,-1],[1,-1]]:
                if 0<=x+i<W+2 and 0<=y+j<H+2:
                    if house[y][x]==0 and house[y+j][x+i]: res+=1
                    if not check[y+j][x+i] and house[y+j][x+i]==0:
                        check[y+j][x+i]=1
                        deq.append([y+j,x+i])
        else:
            for i,j in [[-1,0],[1,0],[-1,-1],[0,-1],[0,1],[-1,1]]:
                if 0<=x+i<W+2 and 0<=y+j<H+2:
                    if house[y][x]==0 and house[y+j][x+i]: res+=1
                    if not check[y+j][x+i] and house[y+j][x+i]==0:
                        check[y+j][x+i]=1
                        deq.append([y+j,x+i])
        
    return res

ans = dfs(0,0)
print(ans)