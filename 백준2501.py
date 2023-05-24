N,K=map(int,input().split())

flag=True
for i in range(1,N+1):
    if N%i==0:
        if K==1:
            print(i)
            flag=False
        K-=1
if flag: print(0)