import sys
input=sys.stdin.readline

from collections import deque

import heapq

heap=[]
heapq.heapify(heap)

N=int(input())

List=[]
for i in range(N):
    List.append(list(map(int,input().split())))


for i in range(N):
    temp=deque([])
    for j in range(N-1,-1,-1):
        temp.append(-List[j][i])
    heapq.heappush(heap,temp)


for i in range(N):
    temp_list=heapq.heappop(heap)
    ans = temp_list.popleft()
    # print(ans)
    if temp_list: heapq.heappush(heap,temp_list)

print(-ans)