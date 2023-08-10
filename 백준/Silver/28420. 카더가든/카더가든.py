import sys
input=sys.stdin.readline

def make_prefix_sum(arr): #가장 최소의 공기 신선도 파악
    DP = [[0 for _ in range(M+1)] for _ in range(N+1)]
 
    for i in range(1, N+1):
        for j in range(1, M+1):
            DP[i][j] = DP[i][j-1] + DP[i-1][j] - DP[i-1][j-1] + arr[i-1][j-1]
    return DP


def prefix_sum(DP, x1, y1, x2, y2):
    #(x1, y1) 부터 (x2, y2)까지의 구간합 구하기
    return DP[x2][y2] - DP[x1-1][y2] - DP[x2][y1-1] + DP[x1-1][y1-1]

def min_prefix_sum(arr,a,b,c):
    res = float("inf")
    prefix_arr=make_prefix_sum(arr)
    #ㄱ모양
    for i in range(1,N-(a+c)+2):
        for j in range(1,M-(b+a)+2):
            current_sum = prefix_sum(prefix_arr,i,j,i+a-1,j+b-1)+prefix_sum(prefix_arr,i+a,j+b,i+a+c-1,j+b+a-1)
            res=min(res,current_sum)
    
    # --나열한 모양
    for i in range(1,N-(a)+2):
        for j in range(1,M-(b+c)+2):
            current_sum = prefix_sum(prefix_arr,i,j,i+a-1,j+b+c-1)
            res=min(res,current_sum)


    return res

N,M=map(int,input().split())
a,b,c=map(int,input().split()) #가로 / 차 세로 / 캠핑카 세로

air=[] # 공기의 신선도를 집어넣는 배열
for _ in range(N):
    air.append(list(map(int,input().split())))

ans=min(min_prefix_sum(air,a,b,c),min_prefix_sum(air,a,c,b))
print(ans)
