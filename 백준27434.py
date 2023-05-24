import sys
input=sys.stdin.readline
N=int(input())
ans=1
for i in range(N,0,-1):
    ans*=i
print(ans)