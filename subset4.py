def subset_sum_exists(A, k, S):
    n = len(A)

    if S == 0 and k == 0:
        return True

    if S != 0 and k == 0:
        return False

    dp = [[0] * (S + 1) for _ in range(k + 1)]
    # DP[i][j]: 정확히 i개의 숫자를 가지고 합이 j가 되게 할 수 있다면 True

    dp[0][0] = 1

    for j in A:
        if j <= S and j>0: #이 때 j가 음수일 때 주의
            dp[1][j] = 1

    for i in range(2, k + 1):
        for j in range(1, S + 1):
            for a in A:
                if j-a<=S and a<=S:
                    if dp[i-1][j-a] == 1 and dp[1][a] == 1:
                        dp[i][j] = 1
                        break
    print(dp)                    
    return dp[k][S] == 1

print(subset_sum_exists([-2, -3, 4, -1, -2, 1, 5, -3],2,11))