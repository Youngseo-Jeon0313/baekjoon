import sys

input=sys.stdin.readline

#그리디야

N,M=map(int,input().split())
List=list(map(int,input().split()))
List.sort(reverse=True)

Box=[0 for _ in range(M)]
for i in List:
    Box[Box.index(min(Box))]+=i
    #print(Box)
print(max(Box))