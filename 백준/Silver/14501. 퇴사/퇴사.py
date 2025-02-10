N = int(input())
DP = [0 for _ in range(N+1)]
for i in range(N):
    a, b = map(int, input().split())
    for j in range(i+a, N+1):
        DP[j] = max(DP[j], DP[i]+b)

print(max(DP))