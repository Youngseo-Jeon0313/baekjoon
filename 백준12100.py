'''
주의해야할 점
완전 계속 옆으로 싹 옮겨야 함

if how==1: #왼쪽으로 쫙
        current_row=0
        current_column=0
        while True:
            #만약 어떤 수가 있다면 이제 여기서부터 움직임 시작! 맨 왼쪽으로 샥샥
                move_column=current_column#현재 col
                while True:
                    if move_column==0 : break
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
                if current_row>=N: break;
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
    print(board)
    return board


'''

 
'''
한 번의 이동에서 이미 합쳐진 블록은 또 다른 블록과 다시 합쳐질 수 없다.


DEEPCOPY 오류!!
'''
import sys
from copy import deepcopy
n=int(input())
Board=[]
for _ in range(n):
    Board.append(list(map(int,input().split())))



def dfs(board,cnt):
    global ans 
    if cnt==5:
        for i in range(n):
            for j in range(n):
                # if board[i][j]>ans: print(board)
                ans=max(ans,board[i][j])
                
                
        return
    if cnt <5:
        for i in [1,2,3,4]:
            tmp_board=move(deepcopy(board),i)
            dfs(deepcopy(tmp_board),cnt+1)
        return

def move(board,how):
    check=[[0] * n for _ in range(n)]

    if how==1:#아래로 내리기
        for j in range(n):
            pointer = n - 1
            for i in range(n - 2, -1, -1):
                if board[i][j] :
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[pointer][j] == 0:
                        board[pointer][j] = tmp
                        if check[i][j]: check[i][j]=0; check[pointer][j]=1;
                    elif board[pointer][j]  == tmp and not check[pointer][j] and not check[i][j]:
                        board[pointer][j] *= 2
                        check[pointer][j]=1
                        pointer -= 1
                    else:
                        pointer -= 1
                        board[pointer][j] = tmp

                
    if how==2: #위로 올리기
        for j in range(n):
            pointer = 0
            for i in range(1, n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[pointer][j] == 0:
                        board[pointer][j] = tmp
                        if check[i][j]: check[i][j]=0; check[pointer][j]=1;
                    elif board[pointer][j]  == tmp  and not check[pointer][j] and not check[i][j]:
                        board[pointer][j] *= 2
                        check[pointer][j]=1
                        pointer += 1
                    else:
                        pointer += 1
                        board[pointer][j]= tmp
    if how==3: #왼쪽으로 쫙        
        for i in range(n):
            pointer = 0
            for j in range(1, n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][pointer] == 0:
                        board[i][pointer] = tmp
                        if check[i][j]: check[i][j]=0; check[i][pointer]=1;
                    elif board[i][pointer]  == tmp and not check[i][pointer] and not check[i][j]:
                        board[i][pointer] *= 2
                        check[i][pointer]=1
                        pointer += 1
                    else:
                        pointer += 1
                        board[i][pointer]= tmp       

    if how==4: #오른쪽으로 쫙
        for i in range(n):
            pointer = n - 1
            for j in range(n - 2, -1, -1):
                if board[i][j] :
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][pointer] == 0:
                        board[i][pointer] = tmp
                        if check[i][j]: check[i][j]=0; check[i][pointer]=1;

                    elif board[i][pointer]  == tmp and not check[i][pointer] and not check[i][j]:
                        board[i][pointer] *= 2
                        check[i][pointer] =1
                        pointer -= 1
                    else:
                        pointer -= 1
                        board[i][pointer] = tmp
    return board


ans=0
dfs(deepcopy(Board),0)
print(ans)

'''
7
2 2 2 2 2 2 2
2 0 2 2 2 2 2
2 0 2 2 2 2 2
2 0 2 2 2 2 2
2 2 2 0 2 2 2
2 2 2 2 2 2 0
2 2 2 2 2 2 0

32


10
0 0 64 32 32 0 0 0 0 0
0 32 32 64 0 0 0 0 0 0
0 0 128 0 0 0 0 0 0 0
64 64 128 0 0 0 0 0 0 0
0 0 64 32 32 0 0 0 0 0
0 32 32 64 0 0 0 0 0 0
0 0 128 0 0 0 0 0 0 0
64 64 128 0 0 0 0 0 0 0
128 32 2 4 0 0 0 0 0 0
0 0 128 0 0 0 0 0 0 0

1024


5
2 0 0 0 0
2 0 0 0 0
4 0 0 0 0 
2 0 0 0 0
2 0 0 0 0
4


문제의 설명 중에

"그 이유는 한 번의 이동에서 이미 합쳐진 블록은 또 합쳐질 수 없기 때문이다." 라는 부분이 있습니다.

즉

2 2 2 2 0 0 0 0은 왼쪽으로 움직이면

4 4 0 0 0 0 0 0 이 됩니다.

8 0 0 0 0 0 0 0 이 되지 않습니다 

'''




