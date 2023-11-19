import heapq

'''bfs'''
N, M, A, B, C = map(int,input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c=map(int,input().split())
    adj[a].append([b,c])
    adj[b].append([a,c])

answer = 0

hq = []
heapq.heappush(hq, [0, -C, A]) # 우선순위 -> 지금까지 나온 최대 요금(최소), 현재 가진 요금(최대), 현재 노드
#deq.append([A, C, 0])
visited = [0 for _ in range(N+1)]
while hq:
    # print(deq)
    fee_max, fee_now, node = heapq.heappop(hq)
    visited[node]=1
    if node == B: 
        answer = fee_max
        break;
    for i in adj[node]:
        if fee_now+i[1]<=0 and not visited[i[0]]:
            heapq.heappush(hq, [max(fee_max,i[1]), fee_now+i[1], i[0]])
            # deq.append([i[0], fee_now-i[1], max(fee_max, i[1])])

if answer ==0: print(-1)
else:
    print(answer)