from heapq import *
import sys
input=sys.stdin.readline


def find(target):
    if target == parent[target]: return target
    #경로 압축 최적화 - 부모노드로 모두 집합!!
    parent[target]=find(parent[target])
    return parent[target]

def union(a,b):
    a = find(a)
    b = find(b)
    #작은 루트 노드 기준으로 합치라!! 같은 그룹으로 묶기
    if a==b: return 
    if a < b: parent[b]=a
    else: parent[a]=b

def dijkstra(s,exitdoor):
    cost = [float('inf')]*(N+1)
    hq = [[0,s]]
    cost[s]=0
    last=0
    while hq:
        t,x = heappop(hq)
        if cost[x] != t: continue
        for nx, nt in adj[x]:
            exitdoor=min(exitdoor,List[nx])
            if cost[nx]>t+nt:
                cost[nx]=t+nt
                last=max(t+nt,last)
                heappush(hq, [cost[nx],nx])
    return [last,exitdoor]



N,M=map(int,input().split())
adj = [[] for _ in range(N+1)]
parent=[i for i in range(N+1)]


for _ in range(M):
    a,b,c=map(int,input().split())
    adj[a].append([b,c])
    union(a,b)
List=list(map(int,input().split()))
List=[0]+List

check=[0 for _ in range(N+1)]
MIN=float('inf')
ans=0
for i in range(1,N+1):
    if check[parent[i]]: continue
    if not check[parent[i]]:
        time,exitdoor=dijkstra(parent[i],List[i])
        check[parent[i]]=1
    ans+=(time+exitdoor)
print(ans)