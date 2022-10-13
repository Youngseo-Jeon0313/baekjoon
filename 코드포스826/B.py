import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    x=int(input())
    if x==3: print(-1)
    else:
        for i in range(x,x-2,-1): print(i,end=' ')
        for j in range(1,x-1): print(j, end=' ')
        print()