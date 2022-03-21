N,M,K,S=map(int,input().split())
p,q=map(int,input().split())
arr=[0]*(N+1)
road=[[]]*(N+1)
for i in range(M):
    a,b=map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

#다익스트라로 위험구간 표시 + dfs
#다익스트라로 1에서 N으로 가는 숙박비 표현 (DP)