import sys
input=sys.stdin.readline

N=int(input())
List=list(map(int,input().split()))

List.sort()
Min=float('inf')
for i in range(N):
    Min=min(Min,List[i]+List[2*N-1-i])
print(Min)