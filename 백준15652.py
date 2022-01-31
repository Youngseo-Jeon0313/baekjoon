def go(x):
    if len(arr) == m :
        print(' '.join(map(str,arr)))
        return
    for i in range(x,n+1):
            arr.append(i)
            go(i)
            arr.pop()

n, m = map(int,input().split())
arr=[]
go(1)