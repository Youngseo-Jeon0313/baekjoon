import sys
input=sys.stdin.readline

MIN,MAX=map(int,input().split())
ans=MAX-MIN+1
a =[True] * (MAX-MIN+1)

# check[0]=False
# if MIN==1: a[0]=False


for i in range(2,int(MAX**0.5)+1):
    k=int(MIN//(i*i))*(i*i)
    for j in range(k,MAX+1,i*i):
        if j>=MIN and j<=MAX:
            if a[j-MIN]:
                a[j-MIN] = False; ans-=1
        
# print(a)
print(ans)


