N=int(input())
List=list(map(int,input().split()))
K=int(input())
target=list(map(int,input().split()))

#init
#DP[추 종류][구슬 무게]=가능 불가능
DP=[[0 for _ in range(40000+1)] for _ in range(N+1)]
DP[0][0]=1

for i in range(N):
    추 =List[i-1]
    for j in range(40000+1):
        if DP[i][j]==1: 
            DP[i+1][j+추]=1
            DP[i+1][j]=1
            DP[i+1][abs(j-추)]=1
for k in target:
    if DP[N][k]==1: print("Y",end=' ')
    else: print("N", end=' ')
print()
