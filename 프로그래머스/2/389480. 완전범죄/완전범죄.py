from copy import deepcopy
def solution(info, n, m):
    answer = 10**6
    # DP[a점수][b점수]=True/False
    DP = [[False for _ in range(140)] for _ in range(140)]
    # init
    DP[0][0]=True
    for i in range(len(info)):
        new_DP = [[0 for _ in range(140)] for _ in range(140)]
        check = 0
        for a in range(140):
            for b in range(140):
                if DP[a][b] :
                    if a+info[i][0] < n:
                        new_DP[a+info[i][0]][b] = True
                    if b+info[i][1] < m:
                        new_DP[a][b+info[i][1]] = True
        DP = deepcopy(new_DP)
        
    for i in range(140):
        for j in range(140):
            if DP[i][j] == True:
                answer = min(answer, i)
    if answer == 10**6: return -1
    return answer