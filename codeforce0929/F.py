T=int(input())
from collections import deque


def bfs(row,col):
    dy = [-1, 1, 0, 0, 1, -1, 1, -1]
    dx = [0, 0, -1, 1, 1, -1, -1, 1]
    
    move = deque()
    move.append([row,col,1])
    
    while move:
        y, x, count = move.popleft()
        visited[y][x] = count
        
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < X and 0 <= nx < Y and not visited[ny][nx] and List[ny][nx]=='*':
                visited[ny][nx] = count+1
                move.append([ny, nx, count+1])






for _ in range(T):
    X,Y=map(int,input().split())
    List=[]
    visited=[[0 for _ in range(Y)] for _ in range(X)]
    for _ in range(X):
        List.append(list(input()))
    value=1
    for i in range(X):
        for j in range(Y):
            if List[i][j]=='*':
                bfs(i,j)
                value+=1

    print(visited)