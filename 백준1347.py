Board=[[0 for _ in range(101)] for _ in range(101)]

N=int(input())
arr=input()

x=51; y=51; direct=0
List=[[51,51]]; Board[51][51]='.'

for i in arr:
    if i=='L': 
        direct=(direct+1)%4
    elif i=='R': 
        direct=(direct+3)%4
    else: 
        if direct==0: y+=1;
        elif direct==1: x+=1;
        elif direct==2: y-=1;
        else: x-=1;
        Board[y][x]='.'
        List.append([x,y])
    # print(i,direct,List)


List.sort(key=lambda x : x[0])
x_min=List[0][0]; x_max=List[-1][0]
List.sort(key=lambda y : y[1])
y_min=List[0][1]; y_max=List[-1][1]

result_board =[['#' for _ in range(x_max-x_min+1)] for _ in range(y_max-y_min+1)]


for i in range(y_min,y_max+1):
    for j in range(x_min,x_max+1):
        if Board[i][j]=='.': result_board[i-y_min][j-x_min]='.'

for i in range(y_min,y_max+1):
    for j in range(x_min,x_max+1):
        print(result_board[i-y_min][j-x_min], end='')
    print()