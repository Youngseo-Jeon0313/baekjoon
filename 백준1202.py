'''
거꾸로 다시 생각
반례
'''
from heapq import *
N,K=map(int,input().split())
List=[]; List2=[];
for _ in range(N):
    a,b=map(int,input().split())
    heappush(List,[a,b])
Bag=[int(input()) for _ in range(K)]
Bag.sort()
sum=0
for i in range(K):  
    flag=False
    while len(List)  :
        if Bag[i]<List[0][0] : break
        x,y=heappop(List)
        heappush(List2,-y)
    if List2:
        sum-=heappop(List2)
print(sum)