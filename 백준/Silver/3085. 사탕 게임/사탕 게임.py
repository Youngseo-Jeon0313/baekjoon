N = int(input())
# N = 50
List = []
for _ in range(N):
    # sample = "ABCDE"*10
    # List.append(list(sample))
    List.append(list(input()))
answer = 0
for i in range(N):
    for j in range(N-1):
        # 두 개를 바꾼다.
        List[i][j], List[i][j+1] = List[i][j+1], List[i][j]
        # 제일 긴 문자열 길이 판단한다.
        DP_row = [[1]*N for _ in range(N)]
        DP_col = [[1]*N for _ in range(N)]
        for a in range(N):
            for b in range(N):
                if (a > 0) and List[a][b] == List[a-1][b] :
                    DP_row[a][b] = DP_row[a-1][b] + 1
                if (b > 0) and List[a][b] == List[a][b-1]:
                    DP_col[a][b] = DP_col[a][b-1] + 1
        answer = max(answer, max([max(DP_row[i]) for i in range(N)]), max([max(DP_col[i]) for i in range(N)]))
        List[i][j], List[i][j+1] = List[i][j+1], List[i][j]
        List[j][i], List[j+1][i] = List[j+1][i], List[j][i]
        DP_row = [[1]*N for _ in range(N)]
        DP_col = [[1]*N for _ in range(N)]
        for a in range(N):
            for b in range(N):
                if (a > 0) and List[a][b] == List[a-1][b] :
                    DP_row[a][b] = DP_row[a-1][b] + 1
                if (b > 0) and List[a][b] == List[a][b-1]:
                    DP_col[a][b] = DP_col[a][b-1] + 1
        answer = max(answer, max([max(DP_row[i]) for i in range(N)]), max([max(DP_col[i]) for i in range(N)]))
        List[j][i], List[j+1][i] = List[j+1][i], List[j][i]

print(answer)
