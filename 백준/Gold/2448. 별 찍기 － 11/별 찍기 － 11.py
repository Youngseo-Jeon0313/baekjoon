def div_conquer(i,j,n):
    #가장 밑 분할 노드 도착했을 때 return
    if n==3:
        star[i][j-2:j+3]='  *  '
        star[i+1][j-2:j+3]=' * * '
        star[i+2][j-2:j+3]='*****'
        return 
    else:
        div_conquer(i,j,n//2)
        div_conquer(i+n//2,j-n//2,n//2)
        div_conquer(i+n//2,j+n//2,n//2)
N=int(input())
star=[[' ' for _ in range(2*N)] for _ in range(N)]

div_conquer(0,N-1,N)
for i in star:
    print(*i,sep='')

