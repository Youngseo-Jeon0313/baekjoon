import sys
input = sys.stdin.readline
t=int(input())

for i in range(t):
    n,m=input().split()
    n=int(n)
    m=int(m)
    print("Scenario #{0}:".format(i+1))
    print((m+n)*(m-n+1)//2)
    print()