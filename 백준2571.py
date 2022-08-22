import sys

input=sys.stdin.readline


N=int(input())
arr=[]
for _ in range(N):
    x,y=map(int,input().split())
    arr.append([x,y])

#arr를 x축을 기준으로 오름차순 정렬한다.

board=[[0 for _ in range(102)] for _ in range(102)]

for i in arr:
    for j in range(100-10-i[1],100-i[1]):
        for k in range(i[0],i[0]+10):
            board[j][k]=1

for i in range(100):
    for j in range(100):
        #높이를 기준으로 누적합
        if i==0: continue
        if not board[i][j]:continue
        board[i][j]=board[i-1][j]+1

#print(board)
#몰라 그냥 100X100X100X100 =1억
ans=0
for i in range(100):
    for j in range(100):
        if not board[i][j]: continue
        #현재 높이가 min높이가 된다. 오른쪽 위로 판단할 예정
        min_height=board[i][j]; i_=i; j_=j
        while True: #오른쪽으로 하나씩 올린다.
            j_+=1; 
            if j_>=100 or board[i_][j_]==0: break;
            min_height=min(min_height,board[i_][j_])
            ans=max(ans, min_height*(j_-j+1))  
                       
print(ans)
        