'''
아메바는 검은색으로 테두리 지어 있음.
'''


def flood_fill():
    check[i][j]=val
    q.append((i,j))
    while q:
        x, y = q.popleft()
        for k in range(8):
            nx, ny = x + d[k][0], y + d[k][1]
            if 0 <= nx < N and 0 <= ny < M:
                if check[nx][ny]==0 and arr[nx][ny]=='1':
                    check[nx][ny]=val
                    q.append((nx, ny))

from collections import deque

while True:
    q=deque()
    M,N=map(int, input().split())
    if M==0 and N==0:
        break
    arr=[]
    for i in range(N):
        arr.append(list(input().split()))

    d = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]
    check=[[0]*M for _ in range(N)]

    val=1
    for i in range(N):
        for j in range(M):
            if check[i][j]==0 and arr[i][j]=='1':
                flood_fill()
                val+=1

    print(val-1)