from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
List = []
for _ in range(N):
    List.append(list(input()))

dx, dy = [0,0,-1,1], [-1,1,0,0]
answer = 0
visited = [[0 for _ in range(M)] for _ in range(N)]

def bfs(start_x,start_y):
    global answer
    deq= deque([])
    deq.append([start_x,start_y])

    while deq:
        x, y = deq.popleft()
        visited[x][y]=1
        for i in range(4):
            nx = x+dx[i]; ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M :
                if not visited[nx][ny] and List[nx][ny] != "X":
                    deq.append([nx,ny]);
                    visited[nx][ny] = 1;
                    if List[nx][ny] =='P':
                        answer+=1

do_x = 0; do_y = 0;
for i in range(N):
    for j in range(M):
        if List[i][j]=='I':
            do_x = i; do_y = j;
# print(visited)

bfs(do_x, do_y)

if answer == 0: print("TT")
else: print(answer)