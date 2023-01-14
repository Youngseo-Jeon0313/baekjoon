import sys
input=sys.stdin.readline

N=int(input())
L=list(map(int,input().split()))

#prefix sum
prefix=[0 for _ in range(N)]


for i in range(N):
    if L[i]==1:
        prefix[i]=prefix[i-1]+1

    else:
        prefix[i]=prefix[i-1]-1
prefix=[0]+prefix
# print(prefix)
print(max(prefix)-min(prefix))