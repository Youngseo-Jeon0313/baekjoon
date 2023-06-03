stand=1
N=int(input())
flag=True
for i in range(40):
    if N==stand: print(1);flag=False
    stand=stand*2
if flag: print(0)