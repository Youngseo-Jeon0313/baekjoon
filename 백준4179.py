'''
시간초과. 굳이 check라는 2차원 배열을 쓰지 않아도 됨
그리고 popleft랑 pop(0)이랑 시간복잡도 차이 존나 남
'''
from collections import deque
R,C=map(int,input().split())
arr=[]
for i in range(R):
    arr.append(list(input()))

def floodfill():
    while F:
        x,y=F.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if 0<=nx<R and 0<=ny<C and arr[nx][ny]=='.':
                    arr[nx][ny]='F'*(len(arr[x][y])+1)
                    F.append((nx,ny))
def floodfill2():
    while J:
        x,y=J.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if 0<=nx<R and 0<=ny<C:
                if arr[nx][ny]=='.':
                    arr[nx][ny]=arr[x][y]+1
                    J.append((nx,ny))
                elif 'F' in str(arr[nx][ny]) and arr[nx][ny]!='#':
                    if len(arr[nx][ny])>arr[x][y]+1:
                        arr[nx][ny]=arr[x][y]+1
                        J.append((nx,ny))
dx,dy=[1,-1,0,0],[0,0,1,-1]
J=deque();F=deque()
for i in range(R):
    for j in range(C):
        if arr[i][j]=='J': 
            if (i==0) or i==R-1 or j==0 or j==C-1: print(1); exit()
            J.append([i,j]); arr[i][j]=1
        elif arr[i][j]=='F': F.append([i,j])

if len(F)>0:
    floodfill()
floodfill2()
print(arr)
MIN=R*C+100
for i in range(C):
        if ('F' not in str(arr[0][i])) and (arr[0][i] != '#') and (arr[0][i]!='.'):
            if arr[0][i]<MIN : MIN=arr[0][i]; flag=True
        if ('F' not in str(arr[R-1][i])) and (arr[R-1][i] != '#') and (arr[R-1][i] != '.'):
            if arr[R-1][i]<MIN: MIN=arr[R-1][i]; flag=True
for j in range(R):
        if  ('F' not in str(arr[j][0])) and (arr[j][0] != '#') and (arr[j][0] != '.'):
            if arr[j][0]<MIN:MIN=arr[j][0]; flag=True
        if  ('F' not in str(arr[j][C-1])) and (arr[j][C-1] != '#') and (arr[j][C-1] != '.'):
            if arr[j][C-1]<MIN:MIN=arr[j][C-1]; flag=True
if MIN==R*C+100 :
    print('IMPOSSIBLE')
else:
    print(MIN)