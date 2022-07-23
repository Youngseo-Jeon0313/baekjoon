import math 
N=int(input())
lst=[]
for i in range(N):
    x,y,v=map(int,input().split())
    lst.append([math.sqrt(x**2+y**2)/v,i])
lst=sorted(lst,key=lambda x: [x[0]])
for j in lst:
    print(j[1]+1)