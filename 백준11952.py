N,M,K,S=map(int,input().split())
p,q=map(int,input().split())
arr=[0]*(N+1)
road=[[] for _ in range(N+1)] #road=[[]]*(N+1) 이거 절대 안 됨 ㅠㅠ
zombie=[]
for j in range(K): zombie.append(int(input()))
for i in range(M):
    a,b=map(int,input().split())
    road[a].append(b)
    road[b].append(a)

def dfs(index,num):
    if num<S:
        for j in road[index]:
            if not visited[j]:
                visited[j]=1
                dfs(j,num+1)

visited=[0]*(N+1)
for i in zombie: 
    dfs(i,0)
print(visited)

#다익스트라로 위험구간 표시 + dfs
#다익스트라로 1에서 N으로 가는 숙박비 표현 (DP)