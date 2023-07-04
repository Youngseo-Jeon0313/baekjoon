import math
n=int(input())
ans=0
for i in range(1,n+1):
    for j in range(1,int(math.sqrt(i))+1):
        if i%j==0: ans+=1
print(ans)