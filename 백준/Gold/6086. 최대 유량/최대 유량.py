import math
 
sz = 128
 
def bfs(flow, capacity, source, sink):
  q = [source]
  parent = [-1] * sz
  parent[source] = source
  while len(q) != 0:
    item = q.pop(0)
    for i in range(sz):
      # parent[i] == -1: i 정점을 아직 방문하지 않았는가?
      if parent[i] == -1 and capacity[item][i] - flow[item][i] > 0:
        q.append(i)
        parent[i] = item
        # 경로를 기억하기 위해 parent 배열 사용 -> item에서 i로 가는 path 가 형성됨
  return parent
 
def maxFlow(capacity, source, sink):
  flow = [[0] * sz for _ in range(sz)]
  rst = 0
  while True:
    # 증가 경로를 못 찾을 때까지 루프를 돈다.
    parent = bfs(flow, capacity, source, sink)
    if parent[sink] == -1: #싱크로 가는 경로가 더 없으면 루프 탈출
      return rst
    p = sink
    amount = math.inf
    while p != source:
      amount = min(amount, capacity[parent[p]][p] - flow[parent[p]][p])
      p = parent[p]
    rst += amount
    p = sink

    # 찾은 flow만큼 해당 경로에 유량 흘려줌
    while p != source:
      flow[parent[p]][p] += amount #flow 되는 부분은 더해주고
      flow[p][parent[p]] -= amount #flow 당하는 부분은 빼준다
      p = parent[p]
 
def solve():
  n = int(input())
  capacity = [[0] * sz for _ in range(sz)]
  for _ in range(n):
    p, q, c = input().split()
    p = ord(p)
    q = ord(q)
    c = int(c)
    capacity[p][q] += c
    capacity[q][p] += c
  print(maxFlow(capacity, ord('A'), ord('Z')))
 
solve()