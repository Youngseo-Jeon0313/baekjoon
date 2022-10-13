import sys
input=sys.stdin.readline


N=int(input())
for _ in range(N):
    x,y=input().split()
    if x[-1]!=y[-1]:
        if ord(x[-1])<ord(y[-1]): print('>')
        elif ord(x[-1])>ord(y[-1]): print('<')
    else:
        if x[-1]=='S':
            if len(x)>len(y): print('<')
            elif len(x)<len(y):print('>')
            else: print('=')
        else:
            if len(x)>len(y): print('>')
            elif len(x)<len(y):print('<')
            else: print('=')
