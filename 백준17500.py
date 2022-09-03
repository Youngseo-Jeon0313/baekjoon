import sys
input=sys.stdin.readline
from collections import deque
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] 
dict={}
def floodfill(val,alpha):
    check[i][j] = val
    q.append((i,j,val))
    while q:
        x, y, val = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if not check[nx][ny] and (arr[nx][ny]=='.' or arr[nx][ny]==alpha) :
                    check[nx][ny] = val
                    q.append((nx, ny,val))

N=int(input())
arr=[]
for _ in range(N):
    arr.append(list(input()))

q=deque()
check=[[0 for _ in range(N)] for _ in range(N)]

key=0
flag=True
for i in range(N):
    for j in range(N):
        if not check[i][j] :
            if arr[i][j]!='.' :
                if arr[i][j] in dict.keys():
                    if (i>0 and j>0 and check[i-1][j-1]==dict[arr[i][j]]) or (i>0 and j<N-1 and check[i-1][j+1]==dict[arr[i][j]]) or (i<N-1 and j>0 and check[i+1][j-1]==dict[arr[i][j]]) or (i<N-1 and j<N-1 and check[i+1][j+1]==dict[arr[i][j]]):
                        flag=False; print(i,j)
                    else:floodfill(dict[arr[i][j]], arr[i][j])
                else:
                    key+=1
                    dict[arr[i][j]]=key
                    floodfill(key,arr[i][j])
print(check)
if flag==False: print(flag,'no')
else: #출력 양식
    printarr=[['' for _ in range(4*N+3)] for _ in range(2*N+3)]
    for i in range(4*N+3): printarr[0][i]='#'; printarr[2*N+2][i]='#'
    for j in range(2*N+3): printarr[j][0]='#'; printarr[j][4*N+2]='#'
    for i in range(1,2*N+3,3):
        for j in range(1,4*N+3,4):
            printarr[i][j]='+'
    for i in range(N):
        for j in range(N):
            printarr[2*i+2][4*j+3]=arr[i][j]
            if i>0 and check[i-1][j]!=check[i][j]: #위가 나랑 달라
                printarr[2*i+1][4*j+2]='-'
                printarr[2*i+1][4*j+3]='-'
                printarr[2*i+1][4*j+4]='-'
            if i<N-1 and check[i+1][j]!=check[i][j]:
                printarr[2*i+3][4*j+2]='-'
                printarr[2*i+3][4*j+3]='-'
                printarr[2*i+3][4*j+4]='-'
            if j>0 and check[i][j-1]!=check[i][j]:
                printarr[2*i+2][4*j+1]='|'
            if j<N-1 and check[i][j+1]!=check[i][j]:
                printarr[2*i+2][4*j+5]='|'        
    
    for k in range(2*N+3):
        for l in range(4*N+3):
            if printarr[k][l]=='': print(' ',end='')
            else:
                print(printarr[k][l],end='')
        print()
