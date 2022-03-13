'''
스도쿠 모양에서 
'''


arr=[list(map(int,input().split())) for _ in range(9)]
nums=[1,2,3,4,5,6,7,8,9]
blank=[]
for i in range(9):
    for j in range(9):
        if arr[i][j]==0:
            blank.append((i,j))

def checkRow(x,a):
    for i in range(9):
        if a==arr[x][i]: return False
    return True
def checkCol(y,a):
    for i in range(9):
        if a==arr[i][y]: return False
    return True

def checkRect(x,y,a):
    nx=x//3*3
    ny=y//3*3
    for i in range(3):
        for j in range(3):
            if a==arr[nx+i][ny+j]:
                return False
    return True

def dfs(idx): #백트래킹
    if idx==len(blank): #blank의 마지막까지 왔다면?
        for i in range(9):
            print(*arr[i])
        exit(0)
    for i in range(1,10):
        x=blank[idx][0]
        y=blank[idx][1]

        if checkRow(x,i) and checkCol(y,i) and checkRect(x,y,i):
            arr[x][y]=i
            dfs(idx+1) 
            arr[x][y]=0 #★★★★다른 경우의수도 보기위해 다시 초기화하고 가는 과정
dfs(0)
