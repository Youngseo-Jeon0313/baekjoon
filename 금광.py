#nXm 크기의 금광이 있다.
#첫번째 열부터 출발하여 매번 오른쪽 위 / 오른쪽 / 오른쪽 아래 로 이동 가능하다.
'''
아이디어
1. 왼쪽 위에서 오는 경우
2. 왼쪽 아래에서 오는 경우
3. 왼쪽에서 오는 경우 
의 세 가지 경우 중 가장 많은 금을 가지고 있는 경우를 테이블에 갱신시켜 준다.

array[i][j] = i행 j열에 존재하는 금의 양
dp[i][j] = i행 j열까지의 최적의 해 (얻을 수 있는 금의 최댓값)
dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j+1])

일대일 대응이다!
'''

for tc in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split())) #일단 배열 값으로 전부 받는다.

    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m]) #줄을 바꿔서 2차원 형식으로 받는다.
        index += m
    for j in range(1, m):
        #왼쪽 위에서 오는 경우
        if i== 0: left_up=0
        else: left_up = dp[i-1][j-1]
        #왼쪽 위에서 오는 경우
        if i== n-1: left_down=0
        else: left_down = dp[i+1][j-1]
        #왼쪽에서 오는 경우
        left=dp[i][j-1]
        dp[i][j]=dp[i][j] + max(left_up, left_down, left)

        result = 0
        for i in range(n):
            result = max(result, dp[i][m-1])
        print(result)
        

'''
1
3 3
1 3 2 6 4 5 8 5 10
10
23
'''