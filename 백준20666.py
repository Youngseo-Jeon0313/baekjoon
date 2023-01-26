import sys
input=sys.stdin.readline

import heapq

N,M=map(int,input().split())
L=list(map(int,input().split()))
L=[0]+L
p=int(input())

heap=[]
heapq.heapify(heap)

check=[0 for _ in range(N+1)]
prerequisite=[[] for _ in range(N+1)]

for i in range(p):
    a,b,c=map(int,input().split())
    L[b]+=c
    prerequisite[a].append([b,c])

for i in range(N):
    heapq.heappush(heap,[L[i+1],i+1])

ans=0
while M>0:
    c=heapq.heappop(heap)
    if check[c[1]]: continue
    check[c[1]]=1

    for i in prerequisite[c[1]]:
        if check[i[0]]: continue
        L[i[0]]-=i[1]
        heapq.heappush(heap,[L[i[0]],i[0]])
    
    ans=max(ans,c[0])

    M-=1
print(ans)