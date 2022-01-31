import sys
input=sys.stdin.readline

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
#자 이제 가로, 세로, 대각선 판단
def garo_check(arr,i,j):
    Garo=''.join(map(str,arr[i][j:j+5]))
    if Garo=='XXXX.'or Garo=='XXX.X' or Garo=='XX.XX' or Garo== 'X.XXX' or Garo=='.XXXX':
            return True
def sero_check(arr,i,j):
    Sero=[]
    Sero.append(arr[i][j])
    Sero.append(arr[i+1][j])
    Sero.append(arr[i+2][j])
    Sero.append(arr[i+3][j])
    Sero.append(arr[i+4][j])
    Sero=''.join(map(str,Sero))
    if Sero=='XXXX.' or Sero=='XXX.X' or Sero== 'XX.XX' or Sero=='X.XXX' or Sero== '.XXXX':
        return True
def diagonal_left(arr,i,j):
    Left=[]
    Left.append(arr[i][j])
    Left.append(arr[i+1][j-1])
    Left.append(arr[i+2][j-2])
    Left.append(arr[i+3][j-3])
    Left.append(arr[i+4][j-4])
    Left=''.join(map(str,Left))
    if Left=='XXXX.' or Left=='XXX.X' or Left=='XX.XX' or Left=='X.XXX' or Left=='.XXXX':
        return True
def diagonal_right(arr,i,j):
    Right=[]
    Right.append(arr[i][j])
    Right.append(arr[i+1][j+1])
    Right.append(arr[i+2][j+2])
    Right.append(arr[i+3][j+3])
    Right.append(arr[i+4][j+4])
    Right=''.join(map(str,Right))
    if Right=='XXXX.' or Right=='XXX.X' or Right=='XX.XX' or Right=='X.XXX' or Right=='.XXXX':
        return True
for i in range(10):
    for j in range(6):
        if garo_check(board,i,j):
            print('1')
            exit()
for i in range(6):
    for j in range(10):        
        if sero_check(board,i,j):
            print('1')
            exit()
for i in range(6):
    for j in range(4,10):
        if diagonal_left(board,i,j):
            print('1')
            exit()
for i in range(6):
    for j in range(6):
        if diagonal_right(board,i,j):
            print('1')
            exit()
    
print('0')