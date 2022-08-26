import sys
input=sys.stdin.readline
MOD=1000000007
N,M=map(int,input().split())

#DP[몇자리수][뭘로 끝나나]
DP=[[0 for _ in range(100001)] for _ in range(N+1)]
for i in range(1,M+1):
    DP[1][i]=i
for i in range(2,N+1):
    for j in range(1,M+1):
        DP[i][j]+=DP[i-1][M]
        DP[i][j]+=DP[i][j-1]
        DP[i][j]%=MOD
        for l in range(j+j,M+1,j):
            #배수에 해당하는 것들을 빼준다.
            DP[i][j]-=(DP[i-1][l]-DP[i-1][l-1]) 
            DP[i][j]%=MOD


# print(DP)
print(DP[N][M]%MOD)