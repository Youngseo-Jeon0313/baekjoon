import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    N=int(input())
    List=list(map(int,input().split()))
    #DP[a에서][b까지의]=min값
    #init
    DP=[[float('inf') for _ in range(N)] for _ in range(N)]
    ANS=[[float('inf') for _ in range(N)] for _ in range(N)]
    '''
    ABCDE
    (A)(BCDE)
    (AB)(CDE)
    (ABC)(DE)
    (ABCD)(E)
    '''
    for i in range(N):
        DP[i][i]=List[i]
        ANS[i][i]=0
    #1차이부터 그 다음 2차이 ...
    for i in range(N):
        for j in range(N-i): 
            if i==1: #차이가 1이라면
                DP[j][j+i]=List[j]+List[j+i]
                ANS[j][j+i]=List[j]+List[j+i]
            else:
                for k in range(j,j+i): #차이만큼에서
                    DP[j][j+i]=min(DP[j][j+i],DP[j][k]+DP[k+1][i+j])
                    ANS[j][j+i]=min(ANS[j][j+i],DP[j][k]+DP[k+1][i+j]+ANS[j][k]+ANS[k+1][i+j])
            # print(DP)
            # print(ANS)

    print(ANS[0][N-1])

