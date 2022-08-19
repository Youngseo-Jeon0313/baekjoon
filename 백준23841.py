
N,M=map(int,input().split())
List=[]
for i in range(N):
    List.append(list(input()))

for i in range(N):
    for j in range(M//2):   
        if List[i][j]!='.' and List[i][M-1-j]=='.':
            List[i][M-1-j]=List[i][j]
        elif List[i][j]=='.' and List[i][M-1-j]!='.':
            List[i][j]=List[i][M-1-j]

for i in List:
    for j in i:
        print(j,end="")
    print()