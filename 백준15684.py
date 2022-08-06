
import sys
input=sys.stdin.readline
N,M,H=map(int,input().split())
Board=[[0 for _ in range(N)] for _ in range(H)] #row(열)이 H, col(행)이 N
for _ in range(M):
    g,s=map(int,input().split())
    Board[g-1][s-1]=1 #그어진 곳을 표시한다.


def check(board):# 현재 board 상태에서 어떤 col에서 나아가도 제자리로 오는지 확인
    for i in range(N): #모든 col에서 확인할 것이다.
        row=0; col=i; #일단 출발은 row가 0일 때부터.
        while row<H:
            #해당 row의 col과 col-1을 살펴보면서 내려간다.
            if col<N and board[row][col]==1:
                col+=1;
            elif col>0 and board[row][col-1]==1:
                col-=1;
            row+=1;
            if col==N+1: return False
        if col!=i: return False
    return True


def dfs(board, res,column):
    global ans
    if check(board): #만약 어디에서든 제자리로 돌아온다는 것이 확인된다면
        if res<=3: ans=min(ans,res); 
        return
    else: #아직 제자리로 돌아오지 못한다.
        if res<3: #res가 3이 넘으면 굳이 가지 않는다.
            for row in range(H):
                for col in range(column,N):
                    if not board[row][col]:
                        if (col==0 and not board[row][col+1]) or (col==N-1 and not board[row][col-1]) or (0<col and col<N-1 and not board[row][col-1] and not board[row][col+1]):
                                board[row][col]=1
                                dfs(board, res+1, col)
                                board[row][col]=0

ans=4
dfs(Board, 0,0) #0번
if ans>3: print(-1)
else:
    print(ans)

'''
시간초과 해결 - dfs 인자에 column 넣기
'''