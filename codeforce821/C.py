T=int(input())
for _ in range(T):
    n=int(input())
    L=list(map(int,input().split()))
    ans=[0 for _ in range(n)]
    check=[0 for _ in range(n)]
    before=-1
    hubo1=[[0,0] for _ in range(n)]
    hubo2=[[0,0] for _ in range(n)]

    for i in range(n):
        if L[i]>=before:
            ans[i]=L[i]; check[i]=1; before=L[i]; 
            hubo1[i][0]=L[i]; hubo1[i][1]=i
            hubo2[i][0]=L[i]; hubo2[i][1]=i
    index=0; value=0
    flag1=False
    for i in range(1,n):
        if check[i]: hubo1[i][0]=hubo1[i-1][0]; hubo1[i][1]=hubo1[i-1][1]
    index=0; value=0
    flag2=False
    for j in range(n-2,-1,-1):
        if check[j]: hubo2[j][0]=hubo2[j+1][0]; hubo2[j][1]=hubo2[j+1][1]
    print(hubo1)
    print(hubo2)
    print(ans)
    flag=False
    for i in range(n):
        if check[i]:
            Flag=True
            if (hubo1[i][0]+L[i])%2==1: 
                ans[i]=hubo1[i][0]; print(i,hubo1[i][1])
            elif (hubo2[i][0]+L[i])%2==1: print(hubo2[i][1],i)
    if not flag: print(0)