'''
AA
AA
위의 모습이 최소 사이클이다.
1 2
4 3 -> 즉, floodfill을 시행했을 때 차이가 최소 3은 나야 함
'''

N, M = map(int,input().split())
List = []
for _ in range(N):
    List.append(list(input()))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

flag = False


def dfs(x,y,value, color):
    global flag
    visited[x][y]=value
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<M :
            if List[nx][ny]==color:
                if visited[nx][ny] and visited[nx][ny]<=value-3:
                    flag = True
                    return
                elif not visited[nx][ny] :
                    dfs(nx,ny,value+1, color)
            

visited = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            dfs(i,j,1,List[i][j])


if flag: print("Yes")
else: print("No")