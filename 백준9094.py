T=int(input())
for _ in range(T):
    N,M=map(int,input().split())
    ans=0
    for i in range(1,N):
        for j in range(i+1,N):
            if (i**2+j**2+M)%(i*j)==0:
                ans+=1
    print(ans)