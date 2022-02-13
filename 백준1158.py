N, step=map(int, input().split())
arr=[]
for i in range(N):
    arr.append(i+1)
a=step-1
i=0
ans=[]
while arr:
    if a>=len(arr):
        while a>=len(arr):
            a-=len(arr)
    ans.append(arr[a])
    arr.pop(a)
    a+=step-1
print('<',end='')
for i in range(len(ans)-1):
    print(ans[i],end=', ')
print(ans[-1],end='')
print('>')