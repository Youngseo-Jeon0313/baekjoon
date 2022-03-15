N,M=map(int,input().split())
arr=[True]*(N+1)
cant=list(map(int,input().split()))
for i in cant: arr[i]=False
coupon=0
costs=[[0,0]]*N
print(costs)
cost=0
for i in range(1,len(arr)+1):
    judge=[]
    if arr[i]==False: judge.append([cost,coupon])
    else:
        if coupon > 0: judge.append([cost,coupon-1])
        judge.append([costs[i-1][0]+10000,coupon])
        if i>=3:judge.append([costs[i-3][0]+25000,coupon+1])
        if i>=5:judge.append([costs[i-5][0]+37000,coupon+2])
    judge.sort(key=lambda x: x[0])
    print(judge)
    costs[i][0]=judge[0][0]; cost=judge[0][0]; coupon=judge[0][1]
    if i==len(arr): print(arr[-1]); break;