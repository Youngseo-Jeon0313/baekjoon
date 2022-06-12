'''
최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는가?
10번 이하로 움직여서 빼낼 수 없다면 -1 출력
'''
import sys
from copy import deepcopy

N,M=map(int,input().split()) #세로 가로
List=[]
for _ in range(N):List.append(list(input()))

flag=False
def dfs(board,cnt):
    global flag
    for i in range(N):
            if 'R' in List[i]: flag=True
            if 'B' in List[i]: flag=False; break
    if flag==False and cnt==10: print(-1); return 
    elif flag==True: print(cnt); return
    for i in range(1,5):
        copyboard=move(deepcopy(board),i)
        dfs(deepcopy(copyboard),cnt+1)

def move(board,how):
    if how==1: #왼쪽으로 쫙
        for i in range(N,-1,-1):
            if board[i]!='R':
                while 

    elif how==2: #오른쪽으로 쫙
    elif how==3: #아래로 쫙
    elif how==4: #위로 쫙
    return board
