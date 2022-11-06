n, a, b = map(int, input().split())

d=[0]*(n+1)
d[0]=1

for i in range(1,n+1):
    if (i!=a and i!=b):
        if i==1:
            d[i]=1
        else:
            d[i]=d[i-2]+d[i-1]
print(d[n])