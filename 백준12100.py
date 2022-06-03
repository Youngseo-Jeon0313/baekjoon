'''
주의해야할 점
완전 계속 옆으로 싹 옮겨야 함

'''
import sys
sys.setrecursionlimit(10**6)
from copy import deepcopy

N=int(input())
Board=[]
for _ in range(N):
    Board.append(list(map(int,input().split())))
def dfs(board,count):
    global ans 
    if count == 5:
        for i in range(N):
            for j in range(N):
                ans=max(ans,board[i][j])
    for i in [1,2,3,4]:
        tmp_board=move(board,i)
        dfs(tmp_board,count+1)
   
    

def move(board,how):
    if how==1: #왼쪽으로 쫙
        current_row=0
        current_column=0
        while True:
            #만약 어떤 수가 있다면 이제 여기서부터 움직임 시작! 맨 왼쪽으로 샥샥
                move_column=current_column#현재 col
                while True:
                    if move_column==0 or current_row==N : break
                    #0에 도달했거나 (맨 왼쪽으로 다 옮겼거나) 아니면 왼쪽에 다른 애 만나면 끝내기
                    elif board[current_row][move_column-1]==board[current_row][move_column]:
                        before=board[current_row][move_column]
                        board[current_row][move_column]=0
                        move_column-=1
                        board[current_row][move_column]=before*2
                    elif board[current_row][move_column-1]==0:
                        board[current_row][move_column-1]=board[current_row][move_column]
                        board[current_row][move_column]=0
                        move_column-=1
                    else:move_column-=1
                current_column+=1
                if current_column==N: current_column=0; current_row+=1; 
                #맨 끝까지 오면 다음 줄로 넘어가서 시행하겠다.
                if current_row>=N:
                    print(board); break;
                    
                #맨 끝 줄까지 오면 끝내겠다
    if how==2: #오른쪽으로 쫙
        current_row=0
        current_column=N-1;
        while True:
            move_column=current_column
            while True:
                if move_column==N-1: break
                elif board[current_row][move_column+1]==board[current_row][move_column]:
                    before=board[current_row][move_column]
                    board[current_row][move_column]=0
                    move_column+=1
                    board[current_row][move_column]=before*2 
                elif board[current_row][move_column+1]==0: board[current_row][move_column+1]=board[current_row][move_column]; board[current_row][move_column]=0; move_column+=1
                else : move_column+=1
            current_column-=1
            if current_column==-1: current_column=N-1; current_row+=1
            if current_row == N :
                print(board); break;
        return
    if how==3: #밑으로 쫙
        current_row=N-1
        current_column=0;
        while True:
            move_row=current_row
            while True:
                if move_row==N-1 :break
                elif board[move_row+1][current_column]==board[move_row][current_column]:
                    before=board[move_row][current_column]
                    board[move_row][current_column]=0
                    move_row+=1
                    board[move_row][current_column]=before*2
                elif board[move_row+1][current_column]==0: board[move_row+1][current_column]=2*board[move_row][current_column]; board[move_row][current_column]=0; move_row+=1
                else: move_row+=1
            current_row-=1
            if current_row==-1: current_row=N; current_column+=1
            if current_column==0: 
                print(board); break;
    if how==4: #위로 쫙
        current_row=0
        current_column=0
        while True:
            move_row=current_row
            while True:
                if move_row==0 : break
                elif board[move_row-1][current_column]==board[move_row][current_column]:
                    before=board[move_row][current_column]
                    move_row-=1
                    board[move_row][current_column]=before*2
                elif board[move_row-1][current_column]==0: board[move_row-1][current_column]=2*board[move_row][current_column]; board[move_row][current_column]=0; move_row-=1
                else: move_row-=1
            current_row+=1
            if current_row==N:current_row=0; current_column+=1
            if current_column==N:
                print(board); break;
    return board
                
    

ans=0
dfs(Board,0)
print(ans)