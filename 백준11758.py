L=[]
for _ in range(3): L.append(list(map(int,input().split())))
x1,y1=L[0]
x2,y2=L[1]
x3,y3=L[2]
ans=x1*y2+x2*y3+x3*y1-(x2*y1+x3*y2+x1*y3)
if ans<0: print(-1)
elif ans>0:print(1)
else:print(0)