'''
코사라주
SCC 발견 조건
자신들의 자식 정점들이 자신의 부모정정므로 갈 수 있는 경우가 없는 경우

SCC 추춮조건
더이상 자식으로는 못 가. 부모에서 나로의 화살표만 있을 때

'''

import sys
sys.setrecursionlimit(10**6)

v, e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(v + 1)]
reverse_graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    # 정방향 그래프 및 역방향 그래프에 주어진 그래프를 추가해준다.
    graph[a].append(b)
    reverse_graph[b].append(a)


# 정방향 dfs, dfs 가 종료되는 노드를 stack 에 쌓는다.
def dfs(node, visited, stack):
    visited[node] = 1
    for ne in graph[node]:
        if visited[ne] == 0:
            dfs(ne, visited, stack)
    stack.append(node)


# 역방향 dfs, 탐색하는 순서대로 stack (scc) 에 쌓는다.
def reverse_dfs(node, visited, stack):
    visited[node] = 1
    stack.append(node)
    for ne in reverse_graph[node]:
        if visited[ne] == 0:
            reverse_dfs(ne, visited, stack)

# 코사라주 알고리즘
stack = []
visited = [0] * (v + 1) 
# 모든 노드에서 정방향 dfs 를 수행한다.
for i in range(1, v + 1):
    if visited[i] == 0:
        dfs(i, visited, stack) # stack에 탐색을 마친 정점 순으로 저장
visited = [0] * (v + 1) # visited 초기화
result = [] # ssc를 담을 result 생성
# 스택이 빌 때까지 pop 되는 요소에서 역방향 dfs 를 진행하여 scc 를 결과에 추가해준다.

while stack:
    #print(stack)
    ssc = []
    node = stack.pop() # stack에서 ssc의 source 추출
    if visited[node] == 0:
        reverse_dfs(node, visited, ssc) # dfs를 돌며 ssc의 source부터 탐색을 진행한다. 탐색한 정점은 ssc에 저장
        result.append(sorted(ssc)) # 재귀가 끝난 정점이 ssc의 sink

print(len(result))
results = sorted(result)
for i in results:
    for j in i:
        print(j,end=' ')
    print('-1')
