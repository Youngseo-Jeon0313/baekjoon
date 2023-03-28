import sys
input=sys.stdin.readline
from collections import deque

T=int(input())
for _ in range(T):
    ans=0
    n=int(input())
    L=list(map(int,input().split()))
    L=sorted(L)
    L=deque(L)
    left=L[0]; right=L[0]
    while len(L)>1:
        a=L.popleft()
        b=L.popleft()
        ans=max(ans,a-left, b-right)
        left=a; right=b
    if L:
        ans=max(ans,L[0]-left,L[0]-right)
    print(ans)