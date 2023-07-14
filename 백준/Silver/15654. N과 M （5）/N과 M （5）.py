def go(arr):
    if len(arr) == m:
        print(' '.join(map(str,arr)))
        return
    for i in range(n):
        if len(arr)==0 or List[i] not in arr:
            arr.append(List[i])
            go(arr)
            arr.pop()
            

n, m = map(int,input().split())
List=list(map(int, input().split()))
List.sort()
go([])