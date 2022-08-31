#놀랍게도 그리디
import sys
input=sys.stdin.readline


N=int(input())
if N==1:print(1)
else:
    print(N+N-2)
for i in range(1,N+1):
    print(1,i)

for j in range(2,N):
    print(N,j)

