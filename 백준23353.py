import sys
input=sys.stdin.readline

N=int(input())
arr=[]
for _ in range(N):
    arr.append(list(map(int,input().split())))

#DP 느낌
ans=[[0 for _ in range(N)]for _ in range(N)]


for i in range(N):
    for j in range(N):
        if arr[i][j]==1:
            tempans=1
            tempi=i; tempj=j
            while tempi<N and tempj<N and arr[tempi][tempj]==1:
                ans[tempi][tempj]=max(ans[tempi][tempj],tempans)
                tempans+=1; tempi+=1; 
            while tempi<N and tempj<N and arr[tempi][tempj]==1:
                ans[tempi][tempj]=max(ans[tempi][tempj],tempans)
                tempans+=1; tempj+=1; 
            while tempi<N and tempj<N and arr[tempi][tempj]==1:
                ans[tempi][tempj]=max(ans[tempi][tempj],tempans)
                tempans+=1; tempi+=1; tempj+=1
            

# print(ans)

MAX=0
#자 열심히 분기
for i in range(N):
    for j in range(N):
        if arr[i][j]==2:
            if i>0:
                MAX=max(MAX,ans[i-1][j]+1)
            if j>0:
                MAX=max(MAX,ans[i][j-1]+1)
            if i<N-1:
                MAX=max(MAX,ans[i+1][j]+1)
            if j<N-1:
                MAX=max(MAX,ans[i][j+1]+1)
            if i>0 and i<N-1 and ans[i-1][j] and ans[i+1][j]:
                MAX=max(MAX,ans[i-1][j]+ans[i+1][j]+1)
            if j>0 and j<N-1 and ans[i][j-1] and ans[i][j+1]:
                MAX=max(MAX,ans[i][j-1]+ans[i][j+1]+1)
            if i>0 and j>0:
                MAX=max(MAX,ans[i-1][j-1]+1)
            if i<N-1 and j<N-1:
                MAX=max(MAX,ans[i+1][j+1]+1)
            if i>0 and i<N-1 and i<N-1 and j<N-1 and ans[i-1][j-1] and ans[i+1][j+1]:
                MAX=max(MAX,ans[i-1][j-1]+1+ans[i+1][j+1])
            MAX=max(MAX,1)
            # print(i,j,MAX)
print(MAX)
