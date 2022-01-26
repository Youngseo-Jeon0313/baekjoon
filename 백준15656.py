def go(arr):
    if len(arr) == m:
        print(' '.join(map(str,arr)))
        return
    for i in range(1, n+1):
            go(arr+[i])

n, m = map(int,input().split())
arr=list(map(int,input().split()))
go([0]*n)