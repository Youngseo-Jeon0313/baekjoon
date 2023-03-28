n=int(input())

flag=True
for i in range(n):
    ans=i
    s=str(i)
    for j in s:
        ans+=int(j)
    if ans==n: print(i); flag=False;break;
if flag: print(0)