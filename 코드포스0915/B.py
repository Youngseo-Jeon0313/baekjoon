import sys
input=sys.stdin.readline

N=int(input())
for _ in range(N):
    n=int(input())
    if n==3:
        print(2,1,3);
    elif n%2==0:
        for i in range((n-2)//2):
            print(2*i+2,2*i+1,end=' ')
        print(n-1,n)
    else:
        print(1,end=' ')
        for i in range(1,(n)//2):
            print(2*i+1,2*i,end=' ')
        print(n-1,n)