N,K=map(int,input().split())
arr=[500000 * 500000]
temp=1; start=N-1;
while True:
    if K>=start:
        K-=start
        arr[start]=temp
        temp+=1; start-=1;
        if K==0:
            while i<=start: arr[i]=temp
