N,K=map(int,input().split())
Ans=[]

for i in range(N):
    L=[]
    n=int(input())
    arr=list(map(int,input().split(' ')))
    for j in range(n):
        x=arr.pop(0)
        y=arr.pop(0)
        L.append(x**2+y**2)
    L.sort()
    Ans.append(L[-1])

Ans.sort()
Ans=Ans[K-1]
print(Ans,'.00',sep='')