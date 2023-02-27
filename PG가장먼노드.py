#얘를 포함해 말아
def solution(triangle):
    DP=[[0 for _ in range(len(triangle))] for _ in range(len(triangle))]
    DP[0][0]=triangle[0][0]
    for i in range(len(triangle)-1):
        for j in range(i+1):
            DP[i+1][j]=max(DP[i+1][j],DP[i][j]+triangle[i+1][j])
            DP[i+1][j+1]=max(DP[i+1][j+1], DP[i][j]+triangle[i+1][j+1])
    # print(DP)
    answer = max(DP[len(triangle)-1])
    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))