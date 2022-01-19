import sys

arr=[]
for line in sys.stdin:
    arr.append(line.split())
    if arr[-1]==['0', '0']:
        break

sinario=1
A=list()
for i in range(len(arr)):
    if arr[i]==['#','0']:
        sinario+=1
    A[sinario]
    