import sys
input=sys.stdin.readline

N=int(input())
a=2**(N+2)-5
a=a%(10**9+7)
print(a)