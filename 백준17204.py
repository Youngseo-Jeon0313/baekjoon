import sys
input=sys.stdin.readline

N,K=map(int,input().split())

Target=[0 for _ in range(N)]
visited=[0 for _ in range(N)]
for i in range(N):
    a=int(input())
    Target[i]=a
ans=0
here=0
while True:
    there=Target[here]
    if visited[there]==1: break;
    ans+=1
    if there==K:print(ans); exit()
    visited[there]=1
    here=there
print(-1)
    