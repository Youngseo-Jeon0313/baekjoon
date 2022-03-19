N,M=map(int,input().split())
arr=[True]*(N+1)
cant=list(map(int,input().split()))
for i in cant: arr[i]=False

coupon=0
costs=[];coupon=[]

for i in range(1,len(arr)):
        if arr[i]==False: 
                costs[i].append([costs[i-1][0],costs[i-1][1]])
        if costs[i-1][1] >= 3: costs[i].append([costs[i-1][0],costs[i-1][1]-3])
        if i>=1: costs[i].append([costs[i-1][0]+10000,costs[i-1][1]])
        if i>=3: costs[i].append([costs[i-3][0]+25000,costs[i-3][1]+1])
        if i>=5:costs[i].append([costs[i-5][0]+37000,costs[i-5][1]+2])
        if i==len(arr)-1: costs[i]=sorted(costs[i], key=lambda x:x[0]); print(costs[i][0])
#62000
print(costs)
