t=int(input())
for _ in range(t):
    n=int(input())
    arr = list(map(int,input().split()))
    check=dict()
    for i in range(n):
        if arr[i] not in check.keys():
            check[arr[i]]=1
        else:
            check[arr[i]]+=1
    answer=-1
    for key, value in check.items():
        if value >=3 : answer=key
    print(answer)
