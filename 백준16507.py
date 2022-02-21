#수학+(그래프에서의 누적합)
import sys
input=sys.stdin.readline
r,c,q=map(int,input().split())
arr =[[*map(int,input().split())] for _ in range(r)]
psum=[[0]*(c+1) for _ in range(r+1)]
for i in range(1, r+1):
    for j in range(1,c+1):
        psum[i][j]=psum[i-1][j]+psum[i][j-1]-psum[i-1][j-1]+arr[i-1][j-1]

for i in range(q):
    r1,c1,r2,c2=map(int,input().split())
    print((psum[r2][c2]-psum[r2][c1-1]-psum[r1-1][c2]+psum[r1-1][c1-1])//((r2-r1+1)*(c2-c1+1)))
