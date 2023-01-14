import sys
input=sys.stdin.readline

N=int(input())
M=int(input())

fibo = [0 for _ in range(N+1)]

fibo[0]=0
fibo[1]=1
if N>1:
    fibo[2]=2

if N>2:
    for i in range(3,N+1):
        fibo[i]=fibo[i-1]+fibo[i-2]
L=[(i+1) for i in range(M)]
no=[]
for _ in range(M):
    x=int(input())
    no.append(x)
ans=1

sum=0
for i in range(1,N+1):
    if (i in no) :
        # print(sum)
        ans*=fibo[sum]
        sum=0
    else:
        sum+=1
    
# print(sum)
ans*=sum
if ans==0: print(1)
else: print(ans)