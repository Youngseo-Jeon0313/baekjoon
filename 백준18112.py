start=int(input())
end=input()
from collections import deque
q=deque
def dfs(q):
    while q:
        num,sum=q.popleft()
        if str(bin(num)[2:])==end: print(sum); break; return;
        q.append([num+1,sum+1])
        q.append([num-1,sum+1])
        if num!=0 :
            a=len(bin(num)[2:])
            for i in range(a+1):
                q.append([num^(1<<i),sum+1])
        print(q)
sum=0
q=deque([])
q.append([start,sum])
dfs(q)