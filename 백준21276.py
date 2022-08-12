import sys
from collections import deque
input = sys.stdin.readline
# 노드의 개수와 간선의 개수 입력

N=int(input())
people=list(input().split())
dict={} #key: 사람 value: 숫자 로 입력
ans={}
for i in range(N): dict[people[i]]=i; ans[people[i]]=[]
#print(dict)
dict_={v:k for k,v in dict.items()}
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (N)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트
graph = [[] for _ in range(N)]

M=int(input())
for _ in range(M):
    a, b = input().split()
    graph[dict[b]].append(dict[a])
    indegree[dict[a]] += 1


visited=[0 for _ in range(N)]
# 위상 정렬 함수
def topology_sort():
    result = []
    q = deque()

    for i in range(N):
        if visited[i]: continue;
        if indegree[i] == 0:
            result.append(dict_[i])
            q.append(i); visited[i]=1
            while q:
                now = q.popleft()
                visited[now]=1
                # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
                for g in graph[now]:
                    indegree[g] -= 1
                    if indegree[g] == 0:
                        q.append(g); 
                        ans[dict_[now]].append(dict_[g])
 

            # 위상 정렬 수행한 결과 출력
    print(len(result))
    result.sort()
    print(*result)
    people.sort()
    for i in people:
        print(i, len(ans[i]),end=' ')
        ans[i].sort()
        print(*ans[i])
topology_sort()