import sys
from collections import deque
dq = deque()
input=sys.stdin.readline

n=int(input())

for i in range(n):
    s=list(input().split())
    if s[0]=='push_front':
        dq.appendleft(s[1])
    elif s[0]=='push_back':
        dq.append(s[1])
    elif s[0]=='pop_front':
        if len(dq)>0:
            x=dq.popleft()
            print(x)
        else:
            print(-1)
    elif s[0]=='pop_back':
        if len(dq)>0:
            x=dq.pop()
            print(x)
        else:
            print(-1)
    elif s[0]=='size':
        print(len(dq))
    elif s[0]=='empty':
        if len(dq)>0:
            print(0)
        else:
            print(1)
    elif s[0]=='front':
        if len(dq) >0:
            print(dq[0])    
        else:
            print(-1)
    elif s[0]=='back':
        if len(dq)>0:
            print(dq[-1])
        else:
            print(-1)