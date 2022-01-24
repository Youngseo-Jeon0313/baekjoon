import sys
input=sys.stdin.readline

t=int(input())
for i in range(t):
    sum=0
    N,M=map(int, input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    B.sort()
    for i in A:
            for j in range(len(B)):
                if i <= B[j]:
                    sum+=len(B)-j
                    break
    print(sum)