import sys
input=sys.stdin.readline

import heapq

N,M=map(int,input().split())
List=[map(int,input().split())]
p=int(input())

prerequisite=[[] for _ in range(N+1)]

for _ in range(p):
    a,b,t=map(int,input().split())
    prerequisite[a].append([b,t])
    List[b-1]+=t

tempList=heapq.heapify(List)
ans=0
while M>0:
    a=heapq.heappop(tempList)
    for i in prerequisite[a]:
        List[i[0]]-=i[1]
    M-=1
'''
처리된 거를 또 처리하지 않도록 주의

'''
print(ans)