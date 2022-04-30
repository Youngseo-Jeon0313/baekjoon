import sys
input=sys.stdin.readline

N,Q =map(int,input().split())
List=map(int,input().split())
dp1=[0]
dp2=[0]
for i in List:
    dp1.append(dp1[-1]+i)
    dp2.append(dp2[-1]+i*i)
for _ in range(Q):
    x,y=map(int,input().split())
    a=dp1[y]-dp1[x-1]
    b=dp2[y]-dp2[x-1]
    print((a*a-b)//2)