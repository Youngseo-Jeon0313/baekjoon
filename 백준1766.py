#전형적인 위상정렬 문제
import heapq
N,M=map(int,input().split())
graph=[[] for _ in range(N+1)] #각 노드에 뭐가 연결되어있는지 표시
inDegree=[0 for _ in range(N+1)] #진입차수
queue = [] #가능한 앞번호부터 라고 했으므로! heap 사용

for i in range(M):
    first,second = map(int,input().split())
    graph[first].append(second)
    inDegree[second]+=1

for i in range(1,N+1):
    if inDegree[i]==0:
        heapq.heappush(queue, i)

while queue:
    tmp = heapq.heappop(queue)
    print(tmp,end=' ')
    for i in graph[tmp]:
        inDegree[i]-=1
        if inDegree[i]==0:
            heapq.heappush(queue,i)
            