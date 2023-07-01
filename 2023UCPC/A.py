
direction=0
for _ in range(10):
    
    a=int(input())
    if a==1: 
        direction=(direction+1)%4
    elif a==2:
        direction=(direction+2)%4
    else:
        direction=(direction+3)%4
if direction==1: print("E")
elif direction==2: print("S")
elif direction==3: print('W')
else: print("N")