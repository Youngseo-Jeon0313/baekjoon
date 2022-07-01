
arr=[]
flag=True
for _ in range(4):
    x1,y1,x2,y2=map(int,input().split())
    if x1>0 and x2>0 :
        arr.append([x1,y1,x2,y2])
    elif x1<0 and x2<0:
        arr.append([x2,y2,x1,y1])
    elif x1<0 and x2>0:
        arr.append([x1,y1,x2,y2])
    else:
        arr.append([x2,y2,x1,x2])


#정렬을 맨 앞 꺼 기준으로
arr1=sorted(arr,key=lambda x:x[0])

if arr1[0][2]<arr1[1][0] : flag=False

if arr1[2][2]<arr1[3][0] : flag=False

arr2=sorted(arr,key=lambda x:x[1])
if arr2[0][3]<arr2[1][1] : flag=False

if arr2[2][3]<arr2[3][1] : flag=False

print(flag)
if flag==True:
    ans=0
    xll=arr1[1][0]
    xlh=min(arr1[1][2],arr1[0][2])
    xhl=arr1[3][0]
    xhh=min(arr1[3][2],arr1[2][2])
    
    yll=arr2[1][1]
    ylh=min(arr2[1][3],arr2[0][3])
    yhl=arr2[3][1]
    yhh=min(arr2[3][3],arr2[2][3])

    for i in range(xll,xlh+1):
        for j in range(xhl,xhh+1):
            for k in range(yll,ylh+1):
                for l in range(yhl,yhh+1):
                    print(i,j,k,l)
                    if j-i==l-k: ans+=1
    #y=x+k
    
    print(xll,xlh,xhl,xhh,yll,ylh,yhl,yhh)
    print(ans)
    #y=x+k
    
else:
    print(0)