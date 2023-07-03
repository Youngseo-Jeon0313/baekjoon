import sys
input=sys.stdin.readline
from collections import deque

N,K=map(int,input().split())
List=[i for i in range(1,N+1)]
List=deque(List)
ans=[]
while List:
    for i in range(K-1):
        List.append(List.popleft())
    ans.append(List.popleft())
print('<',end='')
for i in range(N):
    if i==N-1: print(ans[i],end='') 
    else:print(ans[i],end=', ')
print('>')