board=[]
for i in range(10):
    s=list(input())
    board.append(s)

Apple=[]
for i in range(10):
    for j in range(10):
        if board[i][j]=='X':
            Apple.append([i,j])
print(Apple)
#자 이제 가로, 세로, 대각선 판단
for i in Apple:
    