from collections import deque
import heapq

N=int(input())
s=list(map(int,input().split()))
s.sort()
query=int(input())
heap=[]
heapq.heapify(heap)
for _ in range(query-1):
    x,y=map(int,input().split())
    if x>y:
        heapq.heappush(heap,[-x,'up'])
    else:
        heapq.heappush(heap,[-y,'down'])

lqueryx,lqueryy=map(int,input().split())
ans=''
res=[0 for _ in range(N)]
start=0; end=N-1;
while heap:
    num,how=heapq.heappop(heap)
    num=-num
    if how=='up':
        temp_end=end
        while True:
            if res[temp_end]: break
            res[temp_end]=s[temp_end]
            temp_end+=1
    else:
        temp_start=start
        while True:
            if res[temp_start]: break;
            res[temp_start]=s[temp_start]
            temp_start-=1

print(res)

