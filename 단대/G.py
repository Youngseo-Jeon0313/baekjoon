N=int(input())
arr=list(map(int,input().split()))
Q=int(input())
Qarr=[]
for _ in range(Q):
    Qarr.append(list(map(int,input().split())))

for i in Qarr:
    if i[0]==1:
        for j in range(i[1],i[2]+1):
            ans=