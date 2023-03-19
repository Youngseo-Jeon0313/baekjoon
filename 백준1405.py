import sys
input=sys.stdin.readline

n,E,W,S,N=map(int,input().split())
dx,dy = [-1,1,0,0],[0,0,-1,1]
probs = [E,W,S,N]
#양 옆으로 N만큼 펼쳐진 board 하나 생성
graph = [[0] * (2*n+1) for _ in range(2*n+1)]

def backtracking(x,y,percentage, count):
    graph[x][y]=1
    global answer
    # print(x,y,visited,percentage)
    if count==n:
        answer+=percentage
        return
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not graph[nx][ny]:
            backtracking(nx, ny, percentage*probs[i], count+1)
            graph[nx][ny]=0

answer=0
backtracking(n,n,1,0)
print(answer* (0.01 ** n))