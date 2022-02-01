def flood_fill():
    global sheep
    global wolf
    sheep1=0
    wolf1=0
    #check에다가 val로 표시
    check[i][j] = val
    if arr[i][j]=='o':
        sheep1+=1
    elif arr[i][j]=='v':
        wolf1+=1
    #덱에다가 좌표 set으로 넣기
    q.append((i,j))
    while q:
        #q에 없어질 때까지!! ->  만약에 있으면
        #하나 꺼내
        x, y = q.popleft()
        for k in range(4):
            #그 해당하는 거 오왼좌우
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < row and 0 <= ny < column:
            #영역 안에 들고 / check에 표시 안되어 있으면  표시해주고 q에 또 넣어줌
                if not check[nx][ny]:
                    if arr[nx][ny]=='o': 
                        sheep1+=1
                        check[nx][ny] = val
                        q.append((nx, ny))
                    elif arr[nx][ny]=='v':
                        check[nx][ny]=val
                        wolf1+=1
                        q.append((nx, ny))
                    elif arr[nx][ny]=='.':
                        check[nx][ny]=val
                        q.append((nx,ny))           
    if sheep1>wolf1:
        sheep+=sheep1
    else:
        wolf+=wolf1
from collections import deque
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상하좌우
row,column = map(int,input().split())
arr = []
for i in range(row):
    arr.append(list(input()))
check = [[0]*column for _ in range(row)]
val = 1

q = deque()
sheep=0
wolf=0
for i in range(row):
    for j in range(column):
        #아직 확인 안한 애고 1을 딱 마주쳤을 때
        if check[i][j] == 0 and arr[i][j] != '#':
            flood_fill()
            val+=1
print(sheep,wolf)