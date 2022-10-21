import sys
input=sys.stdin.readline

#입력받기
n,t,m=map(int,input().split())
start,end=map(int,input().split())
#이차원 DP
#DP[그 시간에][여기까지 간 루트에서] = 가장 적은 가중치로 간 것

DP=[[float('inf') for _ in range(n+1)] for _ in range(t+1)]
for i in range(t):
    DP[i][start]=0

for i in range(1,t+1):
    for _ in range(m):
        s,e,w=map(int,input().split())
        DP[i][e]=min(DP[i-1][e],DP[i][e],DP[i-1][s]+w,DP[i][s]+w) #s에서 e
        DP[i][s]=min(DP[i-1][s],DP[i][s],DP[i-1][e]+w,DP[i][e]+w) #e에서 s
        
    


# print(DP)
if DP[t][end]==float('inf'): print(-1)
else:print(DP[t][end])