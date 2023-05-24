n=int(input())
ans=0
for _ in range(n):
    a,b,c,=map(int,input().split())
    L=[a,b,c]
    if len(set(L))==1: ans=max(ans,10000+a*1000)
    elif len(set(L))==2: 
        if a==b: ans=max(ans,1000+a*100)
        elif a==c: ans=max(ans,1000+a*100)
        else: ans=max(ans,1000+b*100)
    else:
        ans=max(ans,max(a,b,c)*100)
print(ans)