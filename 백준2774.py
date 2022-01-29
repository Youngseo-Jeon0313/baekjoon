t=int(input())

for i in range(t):
    s=input()
    arr=[]
    for i in s:
        if i not in arr:
            arr.append(i)
    print(len(arr))