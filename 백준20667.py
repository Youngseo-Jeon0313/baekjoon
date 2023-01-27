import sys
input=sys.stdin.readline

N,M,K=map(int,input().split())

#DP[CPU 사용량][100번에 해당하는 중요도 +++ 올라가는 거임]=메모리 사용량

#init
DP=[[-1 for _ in range(501)] for _ in range(1001)]
DP[0][0]=0
for _ in range(N):
    cpu,memory,priority=map(int,input().split())
    for a in range(M,-1,-1):
        for b in range(500,-1,-1):
            if DP[a][b]!=-1:
                cpu_=min(a+cpu,M); importance=priority+b
                DP[cpu_][importance]=max(DP[cpu_][importance],DP[a][b]+memory)

ans=-1
# print(*DP[M])
for i in range(501):
    if DP[M][i]>=K: ans=i ; break
print(ans)