import sys
input = sys.stdin.readline
List = []
N, K = map(int,input().split())
# DP[i][j]= 동전 종류 i까지 사용해서 j원 만들 때 동전 갯수
DP = [float('inf')]*(K+1)
DP[0] = 0

for i in range(1,N+1): #동전 종류들
    n = int(input())
    List.append(n)

# 바로 전 꺼만 신경쓰면 됨
for i in List:
    for j in range(i, K+1):
        DP[j] = min(DP[j], DP[j-i]+1)

# print(DP)
if DP[K] == float('inf'):
    print(-1)
else:
    print(DP[K])

