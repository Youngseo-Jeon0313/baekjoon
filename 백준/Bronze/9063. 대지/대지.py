n=int(input())
Listx=[]
Listy=[]
for _ in range(n):
    a,b=map(int,input().split())
    Listx.append(a); Listy.append(b)
Listx=sorted(Listx)
Listy=sorted(Listy)
print((Listx[-1]-Listx[0])*(Listy[-1]-Listy[0]))