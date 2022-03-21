N,M=map(int,input().split())
arr=[[]]*N
for _ in range(M):
    a,b=map(int,input().split())
    arr[a]=b
    arr[b]=a
def dfs(index,num):
    if num==4: print(1); exit();
    