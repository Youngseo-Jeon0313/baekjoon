board=[]
for i in range(10):
    s=list(input())
    board.append(s)

Apple=[]
for i in range(10):
    for j in range(10):
        if board[i][j]=='X':
            Apple.append([i,j])
Apple.sort()
print(Apple)
#자 이제 가로, 세로, 대각선 판단
garo=[]
sero=[]
diagonal_right=[]
diagonal_left=[]

for i in range(10):
    for j in range(10):
        if board[i][j]=='X' and garo[-1]==(10*i-1) :
            garo.append(10*i+j)
        elif board[i][j]=='X' and garo[-1]==(10*i-2) and board[i][j-1]=='.':
            garo.append(10*i+j)
        if len(garo)==4:
            if ((garo[-1]==garo[0]+4) or (garo[-1]==garo[0]+3)):
                print('1')
                exit()
            else: garo=[]
        if board[i][j]=='X' and sero[-1]==(10*i-10) :
            sero.append(10*i+j)
        elif board[i][j]=='X' and sero[-1]==(10*i-20) and board[i-1][j]=='.':
            sero.append(10*i+j)
        if len(sero)==4:
            if ((sero[-1]==sero[0]+40) or (sero[-1]==sero[0]+30)):
                print('1')
                exit()
            else: sero=[]
        if board[i][j]=='X' and diagonal_right[-1]==(10*i-11):
            diagonal_right.append(10*i+j)
        elif board[i][j]=='X' and diagonal_right[-1]==(10*i-22) and board[i-1][j-1]:
            diagonal_right.append(10*i+j)
        if len(diagonal_right)==4 :
            if ((diagonal_right[-1]==diagonal_right[0]+44) or (diagonal_right[-1]==sero[0]+33)):
                print('1')
                exit()
            else: diagonal_right=[]
        if board[i][j]=='X' and diagonal_left[-1]==(10*i-9):
            diagonal_left.append(10*i+j)
        elif board[i][j]=='X' and diagonal_left[-1]==(10*i-18) and board[i-1][j+1]=='.':
            diagonal_left.append(10*i+j)
        if len(diagonal_left)==4 :
            if ((diagonal_left[-1]==diagonal_left[0]+44) or (diagonal_left[-1]==sero[0]+33)):
                print('1')
                exit()
            else: diagonal_left=[]
print('0')