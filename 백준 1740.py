sum=0
N=int(input())
N-=1
i=1
while (N-i)>=0:
    N-=i
    i+=1
sum+=3**(i-1)
if N>0:
    sum+=3**(N-1)
print(sum,end='')
