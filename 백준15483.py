def edit_dist(str1, str2):
    dp = [[0] * (len(str2)+1) for _ in range(len(str1) + 1)]
    for i in range(1, len(str1)+1):
        dp[i][0] = i
    for j in range(1, len(str2)+1):
        dp[0][j] = j

    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if str1[i-1] == str2[j-1]: #두 변수가 일치하다면 이전의 편집거리를 가져오면 된다.
                dp[i][j] = dp[i-1][j-1]

            else: #두 변수가 다르다면 이전의 편집거리에서 1 증가. 단 이 때 대각선/왼쪽/위쪽 에서의 값 모두 비교
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

    return dp[-1][-1]

a=input()
b=input()
print(edit_dist(a,b))