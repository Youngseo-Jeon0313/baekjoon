import sys
input=sys.stdin.readline


N,M=map(int,input().split())#투자금 얼마?? / 기업개수

invest=[[0 for _ in range(M)] for _ in range(N+1)]
for _ in range(N):
    L=list(map(int,input().split()))
    for i in range(1,M+1):
        invest[L[0]][i-1]=L[i]

DP=[[0 for _ in range(M)] for _ in range(N+1)]
path=[['' for _ in range(M)] for _ in range(N+1)]

#기업 1에 해당하는 만족도
for j in range(N+1):
    DP[j][0]=invest[j][0]

for i in range(1,N+1):
    path[i][0]=str(i)+str(' ')

for j in range(M):
    path[0][j]=str(0)+str(' ')

# print('invest')
# print(invest)


# print("DP")
# print(DP)
for i in range(1,N+1): #만원
    for k in range(i+1): 
        for j in range(1,M): #기업
            if DP[k][j-1]+invest[i-k][j]>DP[i][j]:
                DP[i][j]=DP[k][j-1]+invest[i-k][j]
                path[i][j]=path[k][j-1]+str(i-k)+str(' ')


# print("DP")
# print(DP)
# print("path")
# print(path)

'''
[[0, 0, 0, 0], [0, 5, 5, 5], [0, 6, 6, 7], [0, 7, 10, 11], [0, 8, 
15, 16]]



4 1
1 5
2 6 
3 7
4 10
10
4
'''
print(DP[-1][-1])
print(path[-1][-1])