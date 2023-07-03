a=input()
status=a[0]
ans=10
for i in range(1, len(a)):
    if a[i]==status: 
        ans+=5
    else: 
        ans+=10
        status=a[i]
print(ans)