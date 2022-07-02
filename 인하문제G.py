import sys
input=sys.stdin.readline


def function(arr):
    flag=True
    #정렬을 맨 앞 꺼 기준으로
    arr1=sorted(arr,key=lambda x:x[0])

    if arr1[0][2]<arr1[1][0] : flag=False

    if arr1[2][2]<arr1[3][0] : flag=False
    arr2=sorted(arr,key=lambda x:x[1])
    if arr2[0][3]<arr2[1][1] : flag=False
    if arr2[2][3]<arr2[3][1] : flag=False

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

        for k in range(yll,yhh):
            sum1=0; sum2=0
            if xll+k<=ylh and xlh+k>=yll and xhl+k<=yhh and xhh+k>=yhl:
                arr=[xll+k,xlh+k,yll,ylh]
                arr=sorted(arr)
                
                sum1+=arr[2]-arr[1]+1
                arr_=[xhl+k,xhh+k,yhl,yhh]
                arr_=sorted(arr_)
                sum2+=arr_[2]-arr_[1]+1
                ans+=sum1*sum2       
        #y=x+k
        print(ans)
    else:
        print(0)



N=int(input())
for _ in range(N):
    arr=[]
    for _ in range(4):
        x1,y1,x2,y2=map(int,input().split())
        if x1<x2 :
            if y1<y2:
                arr.append([x1,y1,x2,y2])
            else:
                arr.append([x1,y2,x2,y1])
        else:
            if y1<y2:
                arr.append([x2,y1,x1,y2])
            else:
                arr.append([x2,y2,x1,y1])
    function(arr)
