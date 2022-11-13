import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    L=list(map(int,input().split()))
    sum_plus=0
    sum_minus=0
    for i in L:
        if i>0: sum_plus+=i
        else: sum_minus-=i
    print(abs(sum_plus - sum_minus))