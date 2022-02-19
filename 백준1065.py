#어차피 1,2,3자리 수 중 하나임
n=int(input())
ans=0
for i in range(1,n+1):
    check=list(str(i))
    if len(check)==1: ans+=1
    elif len(check)==2:
        ans+=1
    else:
        if int(check[0])-int(check[1])==int(check[1])-int(check[2]): ans+=1
print(ans)