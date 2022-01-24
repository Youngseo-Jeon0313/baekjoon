t=int(input())
arr=[]
for i in range(t):
    S,C,L=map(int, input().split())
    arr.append((S,C,L))
arr1=sorted(arr,key = lambda x: [x[0], -x[1], -x[2]])

for i in range(t):
    if arr[i]==arr1[-1]:
        print(i+1)