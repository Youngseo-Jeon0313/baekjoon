import sys 
input=sys.stdin.readline

N=int(input())
arr=[[] for _ in range(N)]
for i in range(N):
    x,y=map(int,input().split())
    arr[i]=[x,y]
arr.sort(key=lambda x:x[0])
ans=0
# print(arr)
for i in range(N):
    ans+=arr[i][0]*(i+1)+arr[i][1]

print(ans)