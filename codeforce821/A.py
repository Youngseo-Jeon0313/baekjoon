T=int(input())
for _ in range(T):
    n,k=map(int,input().split())
    L=list(map(int,input().split()))
    mod=[[] for _ in range(k)]
    for i in range(n): mod[(i+1)%k].append(L[i])
    for i in mod:i.sort(reverse=True)
    mod2=[0 for _ in range(k)]
    for j in range(k): 
        if mod[j]: mod2[j]=mod[j][0]
    # print(mod2)
    for i in range(1,k): 
        mod2[i]+=mod2[i-1]
    print(mod2[-1])