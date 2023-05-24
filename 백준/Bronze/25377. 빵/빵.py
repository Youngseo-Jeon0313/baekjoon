T=int(input())
ans=float("inf")
Flag=False
for _ in range(T):
    a,b=map(int,input().split())
    if a<b: 
        Flag=True
        ans=min(ans,b)
if Flag: print(ans)
else: print("-1")