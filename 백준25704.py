N=int(input())
money=int(input())
ans=1000000
if N>=20:
    ans=min(ans,money//4*3)
if N>=15:
    ans=min(ans,money-2000)
if N>=10: 
    ans=min(ans,money//10*9)
if N>=5:
    ans=min(ans,money-500)
else: ans=money
if ans<0:
    ans=0
print(ans)