import sys
input=sys.stdin.readline

n=int(input())
numList=list(map(int,input().split()))
numList.sort()
if n%2==1:
    print(numList[n//2]**2)
else:
    print(numList[n//2]*numList[n//2-1])