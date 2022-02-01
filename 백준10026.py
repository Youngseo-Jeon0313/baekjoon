'''
적록색인 사람은 빨강과 초록을 똑같이 본다.
'''
import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline

beforeC=0
R=0
G=0
RG=0
B=0

def flood_fill():
    global R,G,RG,B,beforeC
    if beforeC==0 or beforeC=='B':
        if color=='R' or color=='G':
            RG+=1
    if color=='R':
        R+=1; beforeC='R'
    elif color=='G':
        G+=1; beforeC='G'
    elif color=='B':
        B+=1; beforeC='B'
    q.append((i,j))
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if not check[nx][ny] and arr[nx][ny]==color:
                    check[nx][ny] = color
                    q.append((nx, ny))
    beforeC=color
from collections import deque
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상하좌우

arr=[]
RG=0
N = int(input())
for ___ in range(N):
    arr.append(list(input()))
check = [[0]*N for _ in range(N)]


q = deque()
z = deque()

for i in range(N):
    for j in range(N):
        color=arr[i][j]
        if check[i][j]==0:
            flood_fill()
print(check)
print(R+G+B,RG+B)