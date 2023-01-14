import sys
input=sys.stdin.readline

N,M,C=map(int,input().split())
tempList=[list(map(int,input().split())) for _ in range(C)]

CList=[[0 for _ in range(C+1)] for _ in range(C+1)]
for i in range(C+1):
    for j in range(C+1):
        if i==0 or j==0: CList[i][j]=0
        else:
            CList[i][j]=tempList[i-1][j-1]

A=list(map(int,input().split())) 
A=[0]+A
B=list(map(int,input().split()))
B=[0]+B


#DP[A][B] = 이 때까지의 악수 합 중 최고

DP=[[0 for _ in range(M+1)] for _ in range(N+1)]


ans=0

for i in range(1,N+1):
    for j in range(1,M+1):
        DP[i][j] = max(DP[i][j], DP[i-1][j-1]+CList[A[i]][B[j]], DP[i-1][j],DP[i][j-1])
        ans=max(ans,DP[i][j])

# print(DP)
print(ans)
