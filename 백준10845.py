import sys


from collections import deque

q = deque()

order=int(sys.stdin.readline())

for i in range(order):
    s=list(sys.stdin.readline().split)
    if s[0]=='front':
        if len(q)>0:
            print(q[0])
        else:
            print('-1')
    elif s[0]=='back':
        if len(q)>0:
            print(q[-1])
        else:
            print('-1')
    elif s[0]=='size':
        print(len(q))
    elif s[0]=='empty':
        if len(q)>0:
            print(0)
        else:
            print('1')
    elif s[0]=='pop':
        if len(q)>0:
            x=q.popleft()
            print(x)
        else:
            print('-1')
    else:
        q.append(s[1])
