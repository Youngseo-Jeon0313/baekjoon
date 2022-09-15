N=int(input())
for _ in range(N):
    Dict1={i:0 for i in range(1,10)}
    Dict2={i:0 for i in range(1,10)}
    n=int(input())
    arr1=list(input().split())
    arr2=list(input().split())
    sum=0
    arr1.sort()
    arr2.sort()
    # print('arr1',arr1)
    # print('arr2',arr2)
    for x in range(n):
        arr1[x]=str(arr1[x])
        arr2[x]=str(arr2[x])
        if len(arr1[x])>len(arr2[x]):
            arr1[x]=len(arr1[x]); sum+=1
        elif len(arr1[x])<len(arr2[x]):
            arr2[x]=len(arr2[x]) ; sum+=1
        arr1[x]=int(arr1[x])
        arr2[x]=int(arr2[x])
        if arr1[x]>(arr2[x]):
            arr1[x]=1 ; sum+=1
        elif arr1[x]<(arr2[x]):
            arr2[x]=1 ; sum+=1
    print(sum)
    # for x in arr1:
    #     x=str(x)
    #     Dict1[len(x)]+=1
    # for y in arr2:
    #     y=str(y)
    #     Dict2[len(y)]+=1
    # if Dict1[1]!=n:
    #     for i in range(2,10):
    #         if Dict1[i]>0: Dict1[i]-=1; Dict1[1]+=1; sum+=2
    # if Dict2[1]!=n:
    #     for i in range(2,10):
    #         if Dict2[i]>0: Dict2[i]-=1; Dict2[1]+=1; sum+=2
