import sys
imput=sys.stdin.readline

M,N=map(int,input().split())

#init
Board=[[1 for _ in range(M)] for _ in range(M)]


Grow_Board=[0 for _ in range(2*M-1)]

for _ in range(N):
    a,b,c=map(int,input().split())
    for i in range(a,a+b):
        Grow_Board[i] +=1
    for i in range(a+b,2*M-1):
        Grow_Board[i] +=2

for i in range(M):
    Board[M-i-1][0]+=Grow_Board[i]
for j in range(1,M):
    Board[0][j]+=Grow_Board[i+j]

for k in range(1,M):
    for l in range(1,M):
        Board[k][l]+=Board[0][l]-1



for i in range(M):
    print(*Board[i])