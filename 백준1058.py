import sys
input=sys.stdin.readline

#친구니 아니니?
N=int(input())
arr=[list(input()) for _ in range(N)]
friends=[[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j]=='Y':
            friends[i][j]=1
            for k in range(N):
                if arr[j][k]=='Y':
                    if i==k: continue
                    friends[i][k]=1

result=0
for i in friends: result=max(result,sum(i))
print(result)
