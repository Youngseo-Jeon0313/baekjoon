#top down
def fib(n):
    if n<=1:
        return n

    # 계산된적 있을 때 : 캐싱
    if dp[n]:
        return dp[n]

    # 계산된적 없을 때
    dp[n] = fib(n-1) + fib(n-2)
    return dp[n]

