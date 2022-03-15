import sys
input=sys.stdin.readline
'''
게임이론
다들 최선을 다해야 한다..??
'''
def game(x,y,z):
    global flag
    if (x==0 and y==0) or (x==0 and z==0) or (y==0 and z==0): return flag
    if (max(x,y,z)==x and y>0 and z>0) or x==0 : x+=1;y-=1;z-=1; game(x,y,z); flag = not flag;
    elif (max(x,y,z)==y and x>0 and z>0) or y==0: x-=1;y+=1;z-=1; game(x,y,z); flag=not flag;
    elif (max(x,y,z)==z and y>0 and x>0) or z==0: x-=1; y-=1; z+=1; game(x,y,z); flag=not flag;

t=int(input())
for i in range(t):
    flag=True
    x,y,z=map(int,input().split()) 
    minus=min(x,y,z)
    if minus>0: 
        x-=minus; y-=minus; z-=minus;
        if minus%2:flag=not flag;
    game(x,y,z)
    if flag:print('R')
    else: print('B')