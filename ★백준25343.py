#이차원 lis / DP

import sys
input=sys.stdin.readline

N=int(input())
List=[list(map(int,input().split())) for _ in range(N)]
temp=[[1 for _ in range(N)] for _ in range(N)]

check=[[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(i+1):
            for l in range(j+1):
                if List[k][l]<List[i][j]:
                    temp[i][j]=max(temp[i][j],temp[k][l]+1)


# print(temp)
ans=0
for i in temp:
    for j in i:
        if j>ans: ans=j

print(ans)

'''
5 
1 2 3 4 5
2 3 4 5 6
6 5 4 3 2
5 4 3 2 1
4 3 2 1 8
7

1 3 
3 1
2


'''