import sys
input=sys.stdin.readline
'''
제한이 K이므로
이건 배낭문제.!
DP는 이렇게 채워나가면 될 것 같다.
DP[어디마을인지][걸리는시간]=금액

'''
N,K=map(int,input().split())
DP=[[-100 for _ in range(K+1)] for _ in range(N+1)]
DP[0][0]=0
for i in range(1,N+1):
    w, w_money, b, b_money=map(int,input().split())
    for j in range(K+1): 
        if DP[i-1][j]!=-100 :
            if j+w<=K: DP[i][j+w]=max(DP[i][j+w],DP[i-1][j]+w_money)
            if j+b<=K: DP[i][j+b]=max(DP[i][j+b],DP[i-1][j]+b_money)

#print(DP)
ans=0
for a in range(K,-1,-1):
    if DP[N][a]!=-100 :
        ans=max(ans,DP[N][a])
print(ans)