import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    n=int(input())
    L=list(map(int,input().split()))
    prefix_sum=L.copy()
    Ans=n
    for i in range(1,n):
        prefix_sum[i]+=prefix_sum[i-1]
    for i in range(n-1,-1,-1):
        ans=i+1
        a=prefix_sum[i]
        temp=i
        flag=False
        for j in range(i+1,n):
            if prefix_sum[j]-prefix_sum[temp]>a: flag=False; break
            elif prefix_sum[j]-prefix_sum[temp]==a:
                ans=max(ans,j-temp); temp=j; flag=True
            else: flag=False
        if flag:
            # print('?',a)
            Ans=min(Ans,ans)

    print(Ans)

'''

6
1 2 3 4 5 15
'''