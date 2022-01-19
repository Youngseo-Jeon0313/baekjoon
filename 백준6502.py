import sys
import math

arr=[]
for line in sys.stdin:
    arr.append(line.split())
    if arr[-1]==['0']:
        break

for i in range(len(arr)-1):
    if int(arr[i][0])*2 >= math.sqrt(int(arr[i][1])**2+int(arr[i][2])**2):  
        print('Pizza',i+1,'fits on the table.')
    else:
        print('Pizza',i+1,'does not fit on the table.')
