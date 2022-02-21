n, m=map(int,input().split())
arr =[*map(int,input().split())]
lo,hi=1,10**9-1
ans = float('inf')

while lo<=hi:
    mid = (lo+hi)//2
    total=0
    val=0
    for i in range(n):
        if val + arr[i] <= mid:
            val+= arr[i]
        else:
            total+=1
            val=arr[i]
    if val !=0: total +=1
    if max(arr)