import sys
input=sys.stdin.readline

from collections import deque

N=int(input())
for _ in range(N):
    n=int(input())
    L=list(map(int,input().split()))

    q=deque([])
    for i in range(n):
        q.append([L[i],i])
    while len(q)>1:
        x,y=q.popleft()
        x-=1;
        if x>0: q.append([x,y])
    print(q[0][1]+1)