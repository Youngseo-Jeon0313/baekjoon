import sys
input= sys.stdin.readline

N, X = map(int,input().split())
List = list(map(int,input().rstrip().split()))

prefix_sum = [0 for _ in range(N+1)]
for i in range(1,N+1):
    prefix_sum[i]=prefix_sum[i-1]+List[i-1]

ans = 0
ans_count = 0
for j in range(N-X+1):
    if prefix_sum[j+X] - prefix_sum[j] > ans:
        ans = prefix_sum[j+X] - prefix_sum[j]
        ans_count = 1
    elif prefix_sum[j+X] - prefix_sum[j] == ans:
        ans_count+=1

if ans ==0 : print("SAD")
else:
    print(ans)
    print(ans_count)