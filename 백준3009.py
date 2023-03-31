List=[]
a1,a2=map(int,input().split())
b1,b2=map(int,input().split())
c1,c2=map(int,input().split())

if a1==b1: List.append(c1)
elif a1==c1: List.append(b1)
elif b1==c1: List.append(a1)

if a2==b2: List.append(c2)
elif a2==c2: List.append(b2)
elif b2==c2: List.append(a2)

print(*List)