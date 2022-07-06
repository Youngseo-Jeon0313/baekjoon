import math
#gcd를 이용하라고??????하;;;;
def issquare(a,b):
    c=math.gcd(a,b)
    a=a/c;b=b/c
    if int(math.sqrt(a)) == math.sqrt(a) and int(math.sqrt(b))==math.sqrt(b): return True
    else: return False

N=int(input())
arr=list(map(int,input().split()))
flag=True
index=0
arr1=sorted(arr)

for i in range(N):
    if not issquare(arr[i],arr1[i]):
        print("NO"); exit();

print("YES")