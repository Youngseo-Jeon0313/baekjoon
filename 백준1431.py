n=int(input())
arr=[]
for i in range(n): arr.append(input())
arr2=[0 for _ in range(n)]

for i in range(n):
    for j in arr[i]:
        if ord(j)<65 or ord(j)>90:
            arr2[i]+=int(j)
result=[]
for i in range(n):
    result.append([arr[i],arr2[i]])
result.sort(key=lambda x:[len(x[0]),x[1],x[0]])
for i in result: print(i[0])