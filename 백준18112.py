import sys
input=sys.stdin.readline
start=input().strip()
end=input().strip()
from collections import deque
q=deque([])
def dfs(q):
    while q:
        num,sum=q.popleft()
        if str(bin(num)[2:])==end: print(sum); break;
        a=len(bin(num)[2:])
        for i in range(a-1):
            q.append([num^(1<<i),sum+1])
        q.append([num+1,sum+1])
        if num!=0: q.append([num-1,sum+1])
q.append([int(start,2),0])
dfs(q)