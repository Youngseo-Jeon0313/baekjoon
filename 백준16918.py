R,C,N=map(int,input().split())

Board=[]
for i in range(R):
    Board.append(list(input()))

Board1=[["O" for _ in range(C)] for _ in range(R)]
Board2=[["O" for _ in range(C)] for _ in range(R)]
for i in range(R):
    for j in range(C):
        if Board[i][j]=="O":
            Board1[i][j]='.'
            if i>0 :
                Board1[i-1][j]='.'
            if j<C-1:
                Board1[i][j+1]='.'
            if j>0:
                Board1[i][j-1]='.'
            if i<R-1:
                Board1[i+1][j]='.'

for i in range(R):
    for j in range(C):
        if Board1[i][j]=="O":
            Board2[i][j]='.'
            if i>0 :
                Board2[i-1][j]='.'
            if j<C-1:
                Board2[i][j+1]='.'
            if j>0:
                Board2[i][j-1]='.'
            if i<R-1:
                Board2[i+1][j]='.'


if N==1:
    for i in range(R):
        for j in range(C):
            print(Board[i][j],end='')
        print()
elif N%2==0:
    for i in range(R):
        for j in range(C):
            print('O',end='')
        print()

elif N%4==1:
    for i in range(R):
        for j in range(C):
            print(Board2[i][j],end='')
        print()
elif N%4==3:
    for i in range(R):
        for j in range(C):
            print(Board1[i][j],end='')
        print()

'''

문제 예시에서는 파악할 수 없지만 
규칙이
N%4 == 1 /N%4 == 3일 때를 잘 나누어서 파악해야 한다!


'''



'''
더 잘 짜여진 코드!!
for y in range(r):
        for x in range(c):
            if board[y][x]=='O': bombs1[y][x] = '.'
            else :
                for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if y+i>=0 and y+i<r and x+j>=0 and x+j<c and board[y+i][x+j]=='O':
                        bombs1[y][x] = '.'
75~76번째 줄에서 한꺼번에 movemove! 하는 거 잊지 말기         


'''