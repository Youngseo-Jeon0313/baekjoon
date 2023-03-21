import sys
input=sys.stdin.readline

GOAL=int(input())
N=int(input())
compare=0
for _ in range(N):
    a,b=map(int,input().split())
    compare+=a*b

if GOAL==compare: print("Yes")
else: print("No")