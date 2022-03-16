import sys
input=sys.stdin.readline
'''
게임이론
다들 최선을 다해야 한다..??
'''
def turn(x,y,z,f):
    flag=False
    global answer
    if x>0 and y>0: flag=True; turn(x-1,y-1,z+1,f+1); 
    elif x>0 and z>0: flag=True; turn(x-1,y+1,z-1,f+1); 
    elif y>0 and z>0: flag=True; turn(x+1,y-1,z-1,f+1);
    if flag==False: answer=max(answer,f)
    return answer
        
t=int(input())
for i in range(t):
    answer=0
    x,y,z=map(int,input().split()) 
    if y>0 and z>0:
        if x%2==1: x=1
        else: x=2;
    if x>0 and y>0:
        if z%2==1: z=1
        else: z=2
    if x>0 and z>0:
        if y%2==1: y=1
        else: y=2
    turn(x,y,z,answer)
    if answer%2==0: print('R')
    else: print('B')