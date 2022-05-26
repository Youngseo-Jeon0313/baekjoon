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

    if a<=b:
        parent[b]=a
    else:
        parent[a] = b
 
T=int(input())
for _ in range(T):
    N=int(input())
    parent = [i for i in range(N)]
    basket=[]
    for _ in range(N):
        x,y,R=map(int,input().split())
        basket.append([x,y,R])
    
    for i in range(N):
        for j in range(i):
            if ((basket[j][0]-basket[i][0])**2+(basket[j][1]-basket[i][1])**2)<=(basket[j][2]+basket[i][2])**2: union(i,j)

    for i in range(N):
        find(i)

    check=[]
    for i in parent: 
        if i not in check: check.append(i)
    print(len(check))