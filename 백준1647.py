import sys
input=sys.stdin.readline


#최적 경로 압축화
def find(x):
    if parents[x]!=x:
        parents[x]=find(parents[x])
    return parents[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a<b:
        parents[b]=a
    else:
        parents[a]=b

N, M = map(int, input().split())
edges = []

for _ in range(M):
    a, b, value = map(int, input().split())
    edges.append((a, b, value))

# 비용순으로 오름차순
edges.sort(key=lambda x: x[2])

parents = [x for x in range(N+1)]
distance=0; cnt = 0 #찾은 간선의 수
temp_distance=0;
for a, b, value in edges:
    # 해당 간선이 사이클을 만들지 않는다면
    if find(a) != find(b):
        union(a,b)
        distance += value
        temp_distance=value
        cnt += 1
        # N - 1개의 간선을 모두 찾음. 탐색 종료
        if cnt >= N - 1:
            break
    #print(parents)
#그냥 마지막에 넣은 것만 빼면 됨 ㅠㅠㅠㅠㅠㅠ

print(distance-temp_distance)