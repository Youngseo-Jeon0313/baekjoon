import sys
input=sys.stdin.readline
start=input().strip()
end=input().strip()
from collections import deque
q=deque([])
check=[0]*2000
check[int(start,2)]=1
def dfs(q):
    while q:
        num,sum=q.popleft()
        if str(bin(num)[2:])==end: print(sum); break;
        a=len(bin(num)[2:])
        if not check[num+1]: q.append([num+1,sum+1]); check[num+1]=1
        if 0<num<=1024: 
            if not check[num-1]: q.append([num-1,sum+1]); check[num-1]=1
            for i in range(a-1):
                if not check[num^(1<<i)]:q.append([num^(1<<i),sum+1]);  check[num^(1<<i)]=1
q.append([int(start,2),0])
dfs(q)