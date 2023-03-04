#이분탐색의 핵심은 1~N까지의 수 중 어떤 특정 수를 찾으려고 할 때
#쓰는 알고리즘이라는 것이다.

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