n=int(input())
Board=[]
for _ in range(n):
    Board.append(list(map(int,input().split())))

check=[[False] * n for _ in range(n)]

for j in range(n):
            pointer = 0
            for i in range(1, n):
                if Board[i][j]:
                    tmp = Board[i][j]
                    Board[i][j] = 0
                    if Board[pointer][j] == 0:
                        Board[pointer][j] = tmp
                        if check[i][j]: check[i][j]=0; check[pointer][j]=1;
                    elif Board[pointer][j]  == tmp  and not check[pointer][j] and not check[i][j]:
                        Board[pointer][j] *= 2
                        check[pointer][j]=1
                        pointer += 1
                    else:
                        pointer += 1
                        Board[pointer][j]= tmp
print(Board)
print(check)
for i in range(n):
            pointer = n - 1
            for j in range(n - 2, -1, -1):
                if Board[i][j] :
                    tmp = Board[i][j]
                    Board[i][j] = 0
                    if Board[i][pointer] == 0:
                        Board[i][pointer] = tmp
                        if check[i][j]: check[i][j]=0; check[i][pointer]=1;
                    elif Board[i][pointer]  == tmp and not check[i][pointer] and not check[i][j]:
                        Board[i][pointer] *= 2
                        check[i][pointer] =1
                        pointer -= 1
                    else:
                        pointer -= 1
                        Board[i][pointer] = tmp
print(Board)
print(check)