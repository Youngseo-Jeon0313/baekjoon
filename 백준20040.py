#사이클 판단
#union find

import sys
input=sys.stdin.readline
# find 연산
def find(target):
    if target == parent[target]:
        return target
 
    # 경로 압축 최적화
    parent[target] = find(parent[target])
    return parent[target]
 
# union 연산
def union(a, b):
    a = find(a) 
    b = find(b)
 
    # 작은 루트 노드를 기준으로 합침
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N,M=map(int,input().split())

parent = [i for i in range(N)]
 
for j in range(M):
    x,y=map(int,input().split())
    if find(x)==find(y):print(j+1); exit()
    union(x,y)

print(0)