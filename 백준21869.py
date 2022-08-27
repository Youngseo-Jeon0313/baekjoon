#시간초과 떄문에, 돌 때 그리드월드 안에서 흰색 / 검은색 으로 나누어서 돌자


import sys
input=sys.stdin.readline

N=int(input())

visited=[[0 for _ in range(N*3)] for _ in range(2)] #상향대각선 / 하향대각선

def dfs(row,col, res,arr):
    global ans
    global arr1
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
        if res>=ans: ans=res; arr1=arr
        return
    if not visited[0][row+col] and not visited[1][row-col]: #가려는 곳 check
        visited[0][row+col]=1
        visited[1][row-col]=1
        dfs(row,col+2,res+1,arr+[row+1,col+1]);  
        visited[0][row+col]=0
        visited[1][row-col]=0
    #안되면 다음 차례
    dfs(row,col+2,res,arr)

ansarr=[]

ans=0
#체스 판 속 검정색 먼저 판단
arr1=[]
dfs(0,0,0,[]) #0번
print(arr1)
for i in arr1: ansarr.append(i)
res1=ans
ans=0
#체스 판 속 하얀색 판단
arr1=[]
arr2=dfs(0,1,0,[])
print(arr2)
res2=ans
for i in arr1: ansarr.append(i)

print(res1+res2)

