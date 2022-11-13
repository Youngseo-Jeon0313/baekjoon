import sys
input=sys.stdin.readline
 
t=int(input())
for _ in range(t):
    n=int(input())
    if n%2==0:
        print(n//2)
        for i in range(n//2):
            print(3*i+1, 3*n-3*i)
    else:
        print(n//2+1)
        for i in range(n//2):
            print(3*i+1, 3*n-3*i)
        if n==1: i=0; print(1,2)
        else: print(3*(i+1)+1, 3*(i+1)+3)
