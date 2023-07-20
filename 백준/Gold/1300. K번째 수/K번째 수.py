N=int(input())
K=int(input())
start = 1
end = K

while start <= end:
    mid = (start + end) // 2
    num = 0
    for i in range(1,N+1):
        num += min(mid // i, N)
    if num >= K:
        ans = mid ##주의
        end = mid -1
    else:
        start = mid + 1

print(ans)