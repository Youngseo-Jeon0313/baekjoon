import sys
input=sys.stdin.readline

n, s=map(int,input().split())
arr = [*map(int,input().strip().split())]
l,r=0,0
val =0
ans = float('inf')
while True:
    if val >= s:
        ans=min(ans, r-l)
        val-=arr[l]
        l+=1
    elif r==n: break
    else:
        val+=arr[r]
        r+=1
if ans==float('inf'):print(0)
else: print(ans)