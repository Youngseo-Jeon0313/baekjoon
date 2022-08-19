import sys
input=sys.stdin.readline
'''
작은 것을 먼저 방문하고!!!

'''
N,M,V=map(int,input().split())
friends=[[] for _ in range(N+1)]


from collections import deque

visited_d=[0 for _ in range(N+1)]
visited_b=[0 for _ in range(N+1)]

def dfs(node):
    visited_d[node]=1
    for i in friends[node]:
        if not visited_d[i]:
            print(i, end=' ');
            dfs(i)



def bfs(node):
    q=deque()
    q.append(node)
    visited_b[node]=1
    while q:
        a=q.popleft()
        print(a,end=' ')
        for i in friends[a]:
            if not visited_b[i]:
                q.append(i); visited_b[i]=1

for _ in range(M):
    x,y=map(int,input().split())
    friends[x].append(y)
    friends[y].append(x)
for i in friends:
    i.sort()

print(V,end=' ')
dfs(V)
print()
bfs(V)