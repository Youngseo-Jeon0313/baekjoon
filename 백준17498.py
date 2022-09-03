import sys
input=sys.stdin.readline

N,M,D=map(int,input().split()) #행 열 최대점프거리정수

arr=[]
for _ in range(N):
    arr.append(list(map(int,input().split())))

DP=[[-float('inf') for _ in range(M)] for _ in range(N)]
for i in range(M):DP[0][i]=0
for i in range(N):
    for j in range(M):
        for d in range(1,D+1): #거리는 D이하
            for k in range(1,d+1):
                if i-k>=0 and j-(d-k)>=0:
                    DP[i][j]=max(DP[i][j],DP[i-(k)][j-(d-k)]+arr[i-(k)][j-(d-k)]*arr[i][j])
                if i-k>=0 and j+d-k<M: 
                    DP[i][j]=max(DP[i][j],DP[i-(k)][j+(d-k)]+arr[i-(k)][j+(d-k)]*arr[i][j])
                if i-(d-k)>=0 and j-k>=0 and d-k!=0: 
                    DP[i][j]=max(DP[i][j],DP[i-(d-k)][j-(k)]+arr[i-(d-k)][j-(k)]*arr[i][j])
                if i-(d-k)>=0 and j+k<M and d-k!=0: 
                    DP[i][j]=max(DP[i][j],DP[i-(d-k)][j+k]+arr[i-(d-k)][j+k]*arr[i][j])

# print(DP)
print(max(DP[N-1]))