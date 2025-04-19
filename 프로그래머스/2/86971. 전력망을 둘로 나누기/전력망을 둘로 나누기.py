from collections import deque
        
def solution(n, wires):
    adj = [[] for _ in range(n+1)]
    for wire in wires:
        adj[wire[0]].append(wire[1])
        adj[wire[1]].append(wire[0])
    def bfs(start, end):
        check = [False for _ in range(n+1)]
        count = 0
        deq = deque([])
        deq.append(start)
        while deq:
            node = deq.popleft()
            check[node] = 1
            count +=1
            for next_node in adj[node]:
                if next_node == end:
                    continue
                else: 
                    if not check[next_node]:
                        check[next_node] = 1
                        deq.append(next_node)
        return count
    diff = float('inf') # 비슷한 개수
    for wire in wires:
        temp = bfs(wire[0], wire[1])
        # print('temp', temp)
        if abs(n-temp-temp) < diff:
            diff = abs(n-temp-temp)
    return diff