#top down
def fib(n):
    if n<=1:
        return n

    # 계산된적 있을 때 : 캐싱
    if dp[n]:
        return dp[n]
    '''
    사실은
    else:
        fib() 이건데 그게 밑에 있고 그렇게 최대한으로 가면
        n<=1로 가게 됨 저 맨 위 조건
            '''

    # 계산된적 없을 때
    dp[n] = fib(n-1) + fib(n-2)
    return dp[n]

