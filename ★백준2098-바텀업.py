import sys
input=sys.stdin.readline

N=int(input())
List=[]
for _ in range(N):
    List.append(list(map(int,input().split())))

#DP[현재 도시][방문 비트마스킹]=비용
DP=[[float('inf')] *(2**N) for _ in range(N)]
#dfs를 하지 않고 DP bottom up
ans=float('inf')
#초기화 0에서부터 가는 것들.
for i in range(N):
    if List[0][i]: DP[i][1<<i]=List[0][i]

for bits in range(1,1<<N):
    for j in range(N):
        if not (bits&(1<<j)): continue #거기 이미 갔으면 continue
        for k in range(N): #DP테이블에서 가져와서 갱신
            if not (bits&(1<<k)) : continue #거기 이미 갔으면 continue
            if (List[j][k]): DP[k][bits]=min(DP[k][bits], DP[j][bits&~(1<<k)]+List[j][k]);

# print(DP)
for i in range(N):
    ans=min(ans,DP[0][(1 << N) - 1])

print(ans)