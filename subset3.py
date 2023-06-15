def max_subarray_sum_k_or_more(A, k):
    n = len(A)
    max_k_dp = [0] * n
    current_sum = sum(A[:k]) #일단 0에서 k개까지의 합
    max_sum = 0

    for i in range(k, n):
        current_sum += A[i] - A[i-k]
        max_k_dp[i] = current_sum

    dp=[0]*len(A)
    dp[0]=A[0]
    for i in range(1, len(A)):
        dp[i]=max(0, dp[i-1]+A[i])

    for i in range(k, n):
        max_sum = max(max_sum, dp[i]+max_k_dp[i-3])

    return max_sum
print(max_subarray_sum_k_or_more([-2,-3,4,-1,-2,1,5,-3],3))