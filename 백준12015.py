import sys
input=sys.stdin.readline
n=int(input())
List=[]

for _ in range(n):
    x,y=map(int,input().split())
    List.append([x,y])
List.sort(key=lambda x:x[0])

dp=[1]*1000
for i in range(n):
    Max=0
    for j in range(i):
        #증가하기만 하면 그냥 일단 넣기
        if List[i][1]>List[j][1] :
            Max=max(Max, dp[List[j][0]])
    dp[List[i][0]]+=Max

print(n-max(dp))