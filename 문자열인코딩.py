def count_encodings(s):
    n = len(s)
    dp = [0] * (n + 1)  # dp[i]는 문자열 s의 처음부터 i까지의 부분문자열에 대응되는 영어 소문자 문자열의 수를 저장

    # 초기값 설정
    dp[0] = 1  # 빈 문자열은 1개의 영어 소문자 문자열에 대응됨
    if s[0] == '0':  # 첫 번째 문자가 0인 경우는 대응할 수 없으므로 0
        return 0
    dp[1] = 1  # 첫 번째 문자는 1개의 영어 소문자 문자열에 대응됨

    for i in range(2, n + 1):
        # 현재 문자를 단독으로 해석하는 경우
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]

        # 현재 문자와 이전 문자를 함께 해석하는 경우
        two_digits = int(s[i - 2:i])
        if 10 <= two_digits <= 26:
            dp[i] += dp[i - 2]
    print(dp)
    return dp[n]


# 예시 입력: '123'
print(count_encodings('123'))  # 출력: 3
