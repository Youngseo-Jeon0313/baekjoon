#누적합
#완전탐색은 O(NM)인데 누적합은 O(N+M)이다
import sys

input=sys.stdin.readline

n,m=map(int,input().split())
arr = [*map(int,input().split())]

psum=[0]*(n+1)
for i in range(1,n+1):
    psum[i]=psum[i-1]+arr[i-1]

for i in range(m):
    l, r=map(int,input().split())
    print(psum[r]-psum[l-1])