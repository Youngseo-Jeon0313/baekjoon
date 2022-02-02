def flood_fill(arr):
    global X,Y,what
    color=arr[X][Y]
    arr[X][Y]=what #여기도 색칠해주는거 잊지 말기!
    q.append((X,Y))
    while q:
        x, y = q.popleft()
        for dx,dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny]==color:
                    arr[nx][ny]=what
                    q.append((nx, ny))

from collections import deque
q=deque()
N,M=map(int, input().split())
arr=[]
for i in range(N):
    arr.append(list(input()))
X,Y,what=map(int, input().split())

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

flood_fill(arr)

for i in range(N):
    for j in range(M):
        print(arr[i][j],end='')
    print()