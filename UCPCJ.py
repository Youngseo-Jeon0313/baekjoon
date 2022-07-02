def issquare(a,b):
    n=a*b
    tmp=int(n**0.5)
    if tmp**2==n:
            return True
    return False

N=int(input())
arr=list(map(int,input().split()))
flag=True
index=0
arr1=sorted(arr)

for i in range(N):
    if not issquare(arr[i],arr1[i]):
        flag=False

if flag==True: print("YES")
else: print("NO")
            