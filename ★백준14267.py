#두 직원이 같은 직속 상사를 가지는것이 가능
def dfs(x): 
    #누적합으로 상사 한 명의 부하직원들에게 칭찬을 차례대로 또 줌
    for nx in adj[x]:
        cost[nx]+=cost[x] 
        dfs(nx)

import sys
sys.setrecursionlimit(100001)
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[*map(int,input().split())]#상사들 리스트(리스트 번호에 따른)
adj=[[] for _ in range(n)]
cost=[0]*n #1번부터 n번까지의 리스트(0~n-1) 최종 cost 배열

for i in range(1,n):
    adj[arr[i]-1].append(i) #누적합으로 상사들에 직원들을 추가시킴

for i in range(m):
    x, w=map(int,input().split())
    cost[x-1]+=w #부하직원들이 받은 칭찬들을 넣은 list

dfs(0)
print(*cost)