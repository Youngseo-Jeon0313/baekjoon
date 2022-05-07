graph=[(1,2,13),(1,3,5),(2,4,9),(3,4,15),(3,5,3),(4,5,1),(4,6,7),(5,6,2)]
graph.sort(key = lambda x:x[2]) #가중치로 간선 정렬 (정점1, 정점2, 가중치)
mst = []
n=6 #정점의 개수
p=[0] #상호배타적 집합

for i in range(1, n+1):
    p.append(i) #일단 각 정점 자신이 집합의 대표

def find(u):
    if u!=p[u]:
        p[u]=find(p[u]) #경로 압축
    return p[u]

def union(u,v):
    root1=find(u)
    root2=find(v)
    p[root2]=root1

tree_edges=0 #간선 개수
mst_cost=0 #가중치 합

while True:
    if tree_edges == n-1:
        break
    u,v,wt=graph.pop(0)
    if find(u) != find(v):#만약 u와 v가 다른 집합에 속해 있다면
        union(u,v)
        mst.append((u,v))
        mst_cost += wt
        tree_edges +=1

print("최소 신장트리 :", mst)
print('최소신장트리 가중치 : ', mst_cost)