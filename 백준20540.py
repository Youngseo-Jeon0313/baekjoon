a=input()

b=[0,0,0,0]
if a[0]=='E':
    b[0]='I'
if a[0]=="I":
    b[0]='E'
if a[1]=='S':
    b[1]='N'
if a[1]=='N':
    b[1]='S'
if a[2]=='T':
    b[2]='F'
if a[2]=='F':
    b[2]='T'
if a[3]=='J':
    b[3]='P'
if a[3]=='P':
    b[3]='J'

for i in range(4):
    print(b[i], end='')