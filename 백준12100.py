'''
주의해야할 점
완전 계속 옆으로 싹 옮겨야 함

'''

N=int(input())
Board=[]
for _ in range(N):
    Board.append(list(map(int(input().split()))))
def dfs(board,count):
    if count==5: 
        ans=max(ans,)

def move(board,how):
    current_row=0
    current_column=0;
    if how==1: #왼쪽으로 쫙
        while True: 
            if current_column==N: current_column=0; current_row+=1;
            if current_row==N: return board
            if board[current_row,current_column]:
                move_column=current_column
                while True:
                    if board[current_row,move_column-1]!=board[current_row,move_column] or move_column==0: break
                    elif board[current_row,move_column-1]==board[current_row,move_column]:
                        before=board[current_row,move_column]
                        board[current_row,move_column]=0
                        move_column-=1
                        board[move_column,move_column]=before*2
    if how==2: #오른쪽으로 쫙
        while True:
            if current_column==0: current:column=N; current_row+=1
            if current_row ==N:return board
            if board[current_row, current_column]:
                move_column=current_column
                while True:
                    
            

            
            
            

ans=0
dfs(Board,0)
print(ans)