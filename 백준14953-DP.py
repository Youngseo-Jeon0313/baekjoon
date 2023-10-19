import sys
input=sys.stdin.readline

n,m=map(int,input().split())
adj = [[]for _ in range(n)]
real_adj=[[] for _ in range(n)]
#이웃이 몇 개인가 표시
neighbors =[[i,0] for i in range(n)]
neighbors_indextype = [0 for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
    neighbors[a][1]+=1
    neighbors[b][1]+=1
    neighbors_indextype[a]+=1
    neighbors_indextype[b]+=1
for i in range(n):
    for j in adj[i]:
        if neighbors_indextype[j]>neighbors_indextype[i]:
            real_adj[i].append(j)
        elif neighbors_indextype[j]<neighbors_indextype[i]:
            real_adj[j].append(i)
#init
DP = [0 for _ in range(n)]
for i in real_adj:
    for j in i:
        DP[j]=1

flag=True
while flag:
    flag=False
    for i in range(n):
            if DP[i]:
                for k in real_adj[i]:
                    if DP[i]+1>DP[k]:
                        DP[k] = DP[i]+1
                        flag=True

print(max(DP)+1)