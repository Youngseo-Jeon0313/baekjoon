import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n=int(input())
lst = [sorted(list(map(int, input().split()))) for i in range(n)]
lst.sort(key=lambda x: x[1])
# print(lst)
d = int(input())
result = -1
heap = []
for s, e in lst:
    lim = e - d
    if s >= lim:
        heappush(heap, s)
    while heap and heap[0] < lim:
        heappop(heap)
    result = max(result, len(heap))
print(result)

