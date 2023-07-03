N=int(input())
F=int(input())

for i in range(100):
    a=(N//100)*100+i
    if a%F==0: print(str(i).zfill(2)); break;