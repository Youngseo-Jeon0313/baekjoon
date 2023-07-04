ans=0

a,b=input().split()
a=list(a)
b=list(b)
for i in a:
    for j in b:
        ans+=int(i)*int(j)

print(ans)