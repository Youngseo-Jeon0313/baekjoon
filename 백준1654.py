k,n=map(int,input().split())
arr = [int(input()) for i in range(k)]
lo, hi=1, 2**31-1
ans =0
while lo<=hi:
    mid = (lo+hi)//2
    val=0
    for i in range(k):
        val+= arr[i]//mid
    if val>=n:
        ans=max(ans, mid)
        lo=mid+1
    else: hi=mid-1
print(ans)