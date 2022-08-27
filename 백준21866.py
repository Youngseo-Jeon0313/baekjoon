import sys
input=sys.stdin.readline


List=list(map(int,input().split()))
if sum(List)<100: print('none'); exit()
for i in range(9):
    if i==0 or i==1: 
        if List[i]>100: print('hacker');exit()
    if i==2 or i==3:
        if List[i]>200: print('hacker');exit()
    if i==4 or i==5:
        if List[i]>300: print('hacker');exit()
    if i==6 or i==7:
        if List[i]>400: print('hacker');exit()
    if i==8:
        if List[i]>500: print('hacker');exit()
    
print('draw')
    