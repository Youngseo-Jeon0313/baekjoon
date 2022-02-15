t=int(input())
arr=[]
for i in range(t):
    arr.append(int(input()))

d=[0]*13
d[0],d[1],d[2],d[3]=0,1,2,4
for i in range(4,13):
    d[i]=d[i-1]+d[i-2]+d[i-3]

for i in arr:
    print(d[i])