def find_set(x):
    while x != parents[x]:
        x = parents[x]
    return x

N, M = map(int, input().split())
edges = []

for _ in range(M):
    a, b, value = map(int, input().split())
    edges.append((a, b, value))

# 비용순으로 오름차순
edges.sort(key=lambda x: x[2])

parents = [x for x in range(N+1)]
distance=0; cnt = 0 #찾은 간선의 수

for a, b, value in edges:
    # 해당 간선이 사이클을 만들지 않는다면
    if find_set(a) != find_set(b):
        parents[find_set(b)] = find_set(a)
        distance += value
        cnt += 1
        # N - 1개의 간선을 모두 찾음. 탐색 종료
        if cnt >= N - 1:
            break
    print(parents)

print(distance)