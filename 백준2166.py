N=int(input())
L=[]
for _ in range(N): L.append(list(map(int,input().split())))
L.append(L[0])
sum1=0; sum2=0;
for i in range(N):
    sum1+=L[i][0]*L[i+1][1]
    sum2+=L[i][1]*L[i+1][0]
sum=round((sum1-sum2)/2,1)
if sum<0: sum*=-1
print(sum)
