import heapq

a=[]
b=[]
# heapq.heappush(a,1)
# heapq.heappush(a,2)
# heapq.heappush(a,3)
# heapq.heappush(a,4)
# heapq.heappush(a,5)
heapq.heappush(a,6)

heapq.heappush(b,-1)
heapq.heappush(b,-2)
# heapq.heappush(b,-3)
# heapq.heappush(b,-4)
# heapq.heappush(b,-5)
# heapq.heappush(b,-6)

print(heapq.heappop(a)) #1
print(heapq.heappop(b)) #-6
