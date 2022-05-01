#greedy
import heapq
n=int(input())
heap=[]
for _ in range(n):
    heapq.heappush(heap, int(input()))
sum=0
while len(heap)>1:
    a=heapq.heappop(heap)
    b=heapq.heappop(heap)
    sum+=(a+b)
    heapq.heappush(heap, a+b);

print(sum)