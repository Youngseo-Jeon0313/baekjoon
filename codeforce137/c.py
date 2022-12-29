T=int(input())
for _ in range(T):
    n=int(input())
    status = list(input())
    check= [0 for _ in range(n)]
    List = list(map(int,input().split()))
    s=0
    for i in range(n):
        after=0;before=0;
        if status[i]=='1' and not check[i]:
            present=List[i]
            if i<n-1 and status[i+1]=='0':
                after=List[i+1]
            if i>0 and status[i-1]=='0':
                before=List[i-1]
            if after==max(present,after,before) and i<n-1 and status[i+1]=='0' :
                status[i]='0'; status[i+1]='1'; s+=after; check[i+1]=1
            elif before==max(present,after,before) and i>0 and status[i-1]=='0' :
                status[i]='0'; status[i-1]='1'; s+=before; check[i-1]=1
            else: s+=present
        print(s)
    print(s)