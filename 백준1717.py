import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(target):
    if target == parent[target]:
        return target
    #경로 압축 최적화 - 부모노드로 모두 집합!!
    parent[target]=find(parent[target])
    return parent[target]

def union(a,b):
    a = find(a)
    b = find(b)
    #작은 루트 노드 기준으로 합치라!! 같은 그룹으로 묶기
    if a==b: return 
    if a < b:
        parent[b]=a
    else:
        parent[a]=b

N,M=map(int,input().split())
parent=[i for i in range(N+1)]

for _ in range(M):
    x, a, b = map(int,input().split())
    if x ==0: union(a,b)
    else: 
        if find(a)==find(b): print('YES')
        else: print("NO")