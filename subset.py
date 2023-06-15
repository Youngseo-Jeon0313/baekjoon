def subset_sum(nums, target):
    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    # dp[i][j] : 정확하게 i개의 숫자를 가지고 합이 j가 되게 할 수 있다면 True
    # 첫 번째 열 초기화
    for i in range(n + 1):
        dp[i][0] = True
    # 동적 프로그래밍
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if j < nums[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
    
    print(dp)
    return dp[n][target]

# 테스트
nums = [3, 34, 4, 12, 5, 2]
target = 9
is_possible = subset_sum(nums, target)
print(f"부분집합의 합이 {target}인 부분집합이 존재하는가? {is_possible}")

'''
로직
만약 j가 n개의 숫자에 들어있다면 D[1][j]=1

DP[i][j] : 아래 조건을 만족하는 a가 있다면 1
D[i-1][j-a]=1이고 D[1][a]=1
'''

