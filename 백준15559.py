import sys
input=sys.stdin.readline

# find 연산
def find(target): #같은 집합인지 찾는 함수
    if target == parent[target]:
        return target
    # 경로 압축 최적화
    parent[target] = find(parent[target])
    return parent[target]
# union 연산
def union(a, b):
    a = find(a) #이거 빼먹지 않기 주의ㅠㅠㅠㅠ
    b = find(b)
    # 작은 루트 노드를 기준으로 합침
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N,M=map(int,input().split())
List=[]
parent = [i for i in range(N*M)]
# print(parent)
for _ in range(N):
    List.append(list(input()))

for i in range(N):
    for j in range(M):
        if List[i][j]=='S' :
            union(i*M+j, (i+1)*M+j)
        elif List[i][j]=='N':
            union(i*M+j,(i-1)*M+j)
        elif List[i][j]=='E' :
            union(i*M+j,i*M+j+1)
        elif List[i][j]=='W':
            union(i*M+j, i*M+j-1)
num=[0 for _ in range(N*M)]
for i in range(N):
    for j in range(M):
        num[find(i*M+j)]+=1
# print(num)
ans=0
for i in num:
    if i!=0: ans+=1
print(ans)
