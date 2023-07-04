N,Q=map(int,input().split())
arr=[0 for _ in range(10001)]
index=0
for z in range(N):
    a=int(input())
    for i in range(a):
        arr[index+i]=z+1
    index+=a
# print(arr)
for _ in range(Q):
    j=int(input())
    print(arr[j])