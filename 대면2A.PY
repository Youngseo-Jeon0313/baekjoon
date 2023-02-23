import math
import sys
input=sys.stdin.readline


N=int(input())
M=int(input())
ans1=0
ans2=float('inf')
for i in range(N,M+1):
    if (i**(1/2))%1==0:
        ans1+=i
        ans2=min(ans2,i)
if ans1==0: print(-1)
else:
    print(ans1)
    print(ans2)