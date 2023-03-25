import sys
input=sys.stdin.readline

x0, N=map(int,input().split())
for i in range(N):
    if x0%2==0:
        x0=(x0//2)^6
    else:
        x0=(x0*2)^6
    # print(x0)
print(x0)