def findLargestSquareSize(samples):
    N=len(samples); M=len(samples[0])
    DP=[[0 for _ in range(M+1)] for _ in range(N+1)]
    #DP[i][j]:현재 i,j를 정사각형의 맨 오른쪽 아래로 두었을 때의 최대 넓이
    ans=0
    for i in range(1,N+1):
        for j in range(1, M+1):
            if samples[i-1][j-1]==1:
                DP[i][j]=min(DP[i-1][j],DP[i][j-1],DP[i-1][j-1])+1
                ans=max(ans,DP[i][j])
    print(DP)
    return ans*ans


print(findLargestSquareSize([[1,1,1,1,1],[1,1,1,0,0],[1,1,1,0,0],[1,1,1,0,0],[1,1,1,1,1]]))