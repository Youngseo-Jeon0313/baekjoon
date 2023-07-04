N=int(input())
arr=[]
for _ in range(N):
    a,b,c,d=input().split()
    b,c,d=int(b),int(c),int(d)
    arr.append([d,c,b,a])
arr=sorted(arr)
print(arr[-1][-1])
print(arr[0][-1])