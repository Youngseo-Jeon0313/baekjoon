import sys
input=sys.stdin.readline

N,T,C,P=map(int,input().split())
a=N//T
if N%T==0: a-=1

ans=C*P*a
print(ans)