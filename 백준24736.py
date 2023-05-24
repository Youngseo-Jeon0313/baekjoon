list=[]

for _ in range(2):
    a,b,c,d,e=map(int,input().split())
    list.append(6*a+3*b+2*c+d+2*e)
print(*list)