import sys
input=sys.stdin.readline
N=int(input())
List=[list(map(int,input().split())) for _ in range(N)]
#DP[현재 도시][방문 비트마스킹]=비용
DP=[[0] *(1<<N-1) for _ in range(N)]
'''
dfs
파라미터
-비트마스킹
-현재 위치
'''

def dfs(node,bits):
    if DP[node][bits]!=0: 
        return DP[node][bits] #이미 최소로 방문. 메모이제이션
    if bits==(1<<(N-1))-1:
        if List[node][0]:
            return List[node][0]
        else: 
            return float('inf')
    dist=float('inf')
    for i in range(1,N):
        if not List[node][i]: 
            continue
        if bits&(1<<i-1): 
            continue#이미 감
        temp=List[node][i]+dfs(i,bits|(1<<(i-1)))
        if dist>temp:dist=temp
    DP[node][bits]=dist

    return dist


print(dfs(0,0))
