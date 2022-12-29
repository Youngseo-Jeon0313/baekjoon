K,M=map(int,input().split())

L=list(map(int,input().split()))
for _ in range(M):
    P,C=map(int,input().split())
    sum=0
    for i in range(K):
        if L[i]>=P-C and L[i]<=P+C:sum+=1
    print(sum)