mentos=[]

def go(arr):
    if sum(arr)==n and len(arr)==m:
        mentos.append(arr)
    for i in range(1,n):
        if sum(arr)<n and len(arr)<m:
            arr.append(i)
            go(arr)
            arr.pop()

n, m = map(int,input().split())
print(go([]))
print(mentos)