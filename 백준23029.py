import sys
input=sys.stdin.readline

#먹을까 말까
N=int(input())
L=[int(input()) for _ in range(N)]


if N==1: print(L[0])
else:
#0 1만 포함 
#1 1,2를 포함
#2 2만 포함
#DP[현재][0,1,2]=일때 최댓값
    DP=[[0 for _ in range(3)] for _ in range(N+1)] 

    DP[1][0]=L[0]; #1만 포함한 결과
    DP[2][1]=L[0]+L[1]//2; #1, 2를 포함한 결과
    DP[2][2]=L[1]; #2만 포함한 결과

    ans =0

    ans = max(DP[1][0], DP[2][1], DP[2][2])
    if (N>2):
        for i in range(3, N+1):
            DP[i][0] = L[i-1] + max(max(DP[i-3][0], DP[i-3][2]), DP[i-3][1])
            DP[i][2] = L[i-1] + max(max(DP[i-2][0], DP[i-2][2]), DP[i-2][1])
            DP[i][1] = L[i-1]//2 +max(DP[i-1][0], DP[i-1][2])
            ans = max(DP[i][0], DP[i][2], DP[i][1])


    # print(DP)
    print(ans)

