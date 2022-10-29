
T=int(input())
for _ in range(T):
    ans="YES"
    x=int(input())
    s=str(input())
    flag=True
    for i in s:
        if i=='Q': flag=False
        else: 
            flag=True
    if flag==False: ans="NO"
    print(ans)
