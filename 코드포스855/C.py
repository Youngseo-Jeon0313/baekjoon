import sys
input=sys.stdin.readline
from heapq import *

T=int(input())
for _ in range(T):
    ans=0
    N=int(input())
    NumList=list(map(int,input().split()))
    hq=[]
    for i in NumList:
        if i==0:
            if len(hq)==0: continue
            ans-=heappop(hq)
        else:
            heappush(hq,-i)
    print(ans)

