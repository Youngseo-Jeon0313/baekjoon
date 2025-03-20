from collections import deque

dx, dy = [-1,1,0,0],[0,0,-1,1]

def solution(rectangle, characterX, characterY, itemX, itemY):
    for i in rectangle:
        for j in range(4):
            i[j]*=2
    characterX *=2
    characterY *=2
    itemX*=2
    itemY*=2    
    
    max_y=0; max_x=0;
    for i in (rectangle): #y
        max_y = max(max_y, i[1], i[3])
        max_x = max(max_x, i[0], i[2])
    board = [[-1 for _ in range(max_x+1)] for _ in range(max_y+1)]
    visited = [[0 for _ in range(max_x+1)] for _ in range(max_y+1)]
    for i in rectangle:
        x1, y1, x2, y2 = i
        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                if x1<x<x2 and y1<y<y2:
                    board[y][x]=0
                elif board[y][x]!=0:
                    board[y][x]=1
                

    q = deque([])
    answer =[]
    q.append([characterY, characterX,1]) #y,x,몇번째 step
    while q:
        curr_y,curr_x,step = q.popleft()
        visited[curr_y][curr_x]=step
        for i in range(4):
            ny, nx = curr_y+dy[i], curr_x+dx[i]
            if ny<0 or nx<0 or ny>max_y or nx>max_x:
                continue
            if ny==itemY and nx==itemX:
                visited[ny][nx]=step+1
                answer.append(step+1)
            elif board[ny][nx]==1:
                if not visited[ny][nx]:
                    visited[ny][nx]=step+1
                    q.append([ny,nx,step+1])
    #print(answer)
    return (min(answer)-1)//2
