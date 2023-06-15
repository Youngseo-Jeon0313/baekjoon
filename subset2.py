arr=list(map(int,input().split()))
dp=[0]*len(arr)
dp[0]=arr[0]
for i in range(1, len(arr)):
    dp[i]=max(0, dp[i-1]+arr[i])
print(max(dp))


def max_subarray_sum_k(A, k):
    n = len(A)
    dp = [0] * n
    current_sum = sum(A[:k]) #일단 0에서 k개까지의 합

    for i in range(k, n):
        current_sum += A[i] - A[i-k]
        dp[i] = current_sum
    print(dp)
    return max(dp)

print(dp)

print(max_subarray_sum_k([-2,-3,4,-1,-2,1,5,-3],3))