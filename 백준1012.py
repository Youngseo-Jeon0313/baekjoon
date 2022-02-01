def flood_fill():
    #check에다가 val로 표시
    check[i][j] = val
    #덱에다가 좌표 set으로 넣기
    q.append((i,j))
    while q:
        #q에 없어질 때까지!! ->  만약에 있으면
        #하나 꺼내
        x, y = q.popleft()
        for k in range(4):
            #그 해당하는 거 오왼좌우
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
            #영역 안에 들고 & check에 표시 안되어 있으면  표시해주고 q에 또 넣어줌
                if arr[nx][ny] and not check[nx][ny]:
                    check[nx][ny] = val
                    q.append((nx, ny))

from collections import deque
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상하좌우

t = int(input())
for ___ in range(t):
    m, n, k = map(int,input().split())
    arr = [[0]*m for _ in range(n)]
    for i in range(k):
        y, x = map(int,input().split())
        #입력받은 것들 1로 바꾸기
        arr[x][y] = 1
    check = [[0]*m for _ in range(n)]
    val = 1

    q = deque()
    for i in range(n):
        for j in range(m):
            #아직 확인 안한 애고 1을 딱 마주쳤을 때
            if check[i][j] == 0 and arr[i][j] == 1:
                flood_fill()
                val += 1
    print(val - 1)