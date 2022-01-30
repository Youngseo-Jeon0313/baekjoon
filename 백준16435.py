import sys
input=sys.stdin.readline

n, length=map(int, input().split())
L=list(map(int, input().split()))
L.sort()
for i in range(len(L)):
    if length>=L[i]:
        length+=1

print(length)