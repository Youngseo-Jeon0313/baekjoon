#시간초과 떄문에, 돌 때 그리드월드 안에서 흰색 / 검은색 으로 나누어서 돌자


import sys
input=sys.stdin.readline

N=int(input())

Board=[list(map(int,input().split())) for _ in range(N)] 
visited=[[0 for _ in range(N*3)] for _ in range(2)] #상향대각선 / 하향대각선

def dfs(row,col, res):
    global ans
    #번갈아가면서 왔다갔다 
    #흰 검 흰 검
    #검 흰 검 흰
    if N%2==1:
        if col==N:
            row+=1; col=0 
        elif col==N+1:
            row+=1; col=1
    else:
        if col==N:
            row+=1; col=1
        elif col==N+1:
            row+=1; col=0
    if row==N : 
        #print(visited)
        ans=max(ans,res); return
    if Board[row][col] and not visited[0][row+col] and not visited[1][row-col]: #가려는 곳 check
        visited[0][row+col]=1
        visited[1][row-col]=1
        dfs(row,col+2,res+1)
        visited[0][row+col]=0
        visited[1][row-col]=0
    #안되면 다음 차례
    dfs(row,col+2,res)
ans=0
#체스 판 속 검정색 먼저 판단
dfs(0,0,0) #0번
res1=ans
ans=0
#체스 판 속 하얀색 판단
dfs(0,1,0)
res2=ans

print(res1+res2)
