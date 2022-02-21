from collections import deque
q=deque()
N=int(input())
while True:
    a=int(input())
    if a==-1: break
    elif a==0: 
        q.popleft()
    else:
        if len(q)<N:q.append(a)
if len(q)==0: print('empty'); 
else: 
    for i in q: print(i, end=' ')