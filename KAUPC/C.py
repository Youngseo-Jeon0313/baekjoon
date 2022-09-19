import sys
input=sys.stdin.readline

N,K=map(int,input().split())
can=list(map(int,input().split()))

Langi=[]
Merry=[]

for _ in range(K):
    Langi.append(list(map(int,input().split())))
for _ in range(K):
    Merry.append(list(map(int,input().split())))



DP=[[[0 for _ in range(2**(N+1)-1)] for _ in range(9)] for _ in range(N)]
#DP[몇번째캔][캔 개수][비트마스킹 몇 번째 날을 줬는가]=최상값

#init 
for i in range(9):
    DP[i][1][1<<i]=1



for i in range(N):
    for j in range(can[i]):
        for k in range(2**(N+1)-1):
            for l in range(9):
                #만약 특정 구간을 안 갔다면
                if k&(1<<l)==0:
                    DP[i][j][k|(1<<l)]=
                