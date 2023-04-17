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