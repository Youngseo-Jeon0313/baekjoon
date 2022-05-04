#재귀...
'''
쉽지 않은 dfs 문제인 것 같다..
처음 보는 것 같은데??
재귀를 잘 사용할 줄 알아야 한다.

'''
import sys
input= sys.stdin.readline
import heapq
N,M=map(int,input().split())

arr=[]
for _ in range(N):arr.append(list(map(int,input().split()) ))
dp=[[0 for col in range(M)] for row in range(N)]
dp[0][0]=1

q=[]
heapq.heappush(q,[-arr[0][0],0,0])
while q:
    x,i,j=heapq.heappop(q)
    for nx, ny in [-1,0],[1,0],[0,-1],[0,1]:
        if 0<=i+nx<N and 0<=j+ny<M and arr[i+nx][j+ny]<arr[i][j] :
            if dp[i+nx][j+ny]==0:heapq.heappush(q,[-arr[i+nx][j+ny],i+nx,j+ny])
            dp[i+nx][j+ny]+=dp[i][j]
print(dp[N-1][M-1])
