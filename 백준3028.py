cup=input()
CUP=[1,0,0]
for i in cup:
    if i=='A':
        CUP[0],CUP[1]=CUP[1],CUP[0]
    elif i=='B':
        CUP[1],CUP[2]=CUP[2],CUP[1]
    else:
        CUP[0],CUP[2]=CUP[2],CUP[0]
for i in range(3):
    if CUP[i]: print(i+1)