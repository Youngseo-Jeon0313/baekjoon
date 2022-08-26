import json
import sys
input=sys.stdin.readline

N=int(input())
List=[]
for _ in range(N):
    x,y=map(int,input().split())
    List.append([x,y])
#DP[a에서][b까지의]=min값
#init
DP=[[float('inf') for _ in range(N)] for _ in range(N)]

'''
ABCDE
(A)(BCDE)
(AB)(CDE)
(ABC)(DE)
(ABCD)(E)
'''
for i in range(N):
    DP[i][i]=0
#1차이부터 그 다음 2차이 ...
for i in range(N):
    for j in range(N-i): 
        if i==1: #차이가 1이라면
            DP[j][j+i]=List[j][0]*List[j+i][0]*List[j+i][1]
        else:
            for k in range(j,j+i): #차이만큼에서
                DP[j][j+i]=min(DP[j][j+i],DP[j][k]+DP[k+1][j+i]+List[j][0]*List[k][1]*List[i+j][1])
        #print(DP)
#print(DP)
print(DP[0][N-1])