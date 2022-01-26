def go(check, start):
    if sum(check) == m:
        ans = [arr[i] for i in range(n) if check[i]]
        print(' '.join(map(str,ans)))
        return
    for i in range(start, n):
        if check[i] == 0:
            check[i] = 1
            go(check, i+1)
            check[i] = 0

n, m = map(int,input().split())
arr = sorted(list(map(int,input().split())))
go([0]*n, 0)