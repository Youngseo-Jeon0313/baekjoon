import sys
input = sys.stdin.readline

def find(a):
    if a == parent[a]: 
        return a
    parent[a] = find(parent[a])  
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    # a , b의 루트노드를 찾아줌
    if b < a:
        parent[a] = b
    else:
        parent[b] = a

n,m=map(int,input().split())
arr = []
parent = [i for i in range(n + 1)]
ans = 0
for i in range(m):
    a, b, c = map(int, input().split())
    arr.append([c,a,b,])
    ans += c

arr.sort(key=lambda x: -x[0]) # 사용자가 많은 다리들을 우선으로 살린다.
for dis, a, b in arr:
    if find(a) != find(b):  # 루트가 같으면 할 필요가 없음
        union(a, b)
        ans -= dis # 전체 사람들 - 사용할 수 있는 사람들


print(ans) #폭파하여 피해를 본 사람들