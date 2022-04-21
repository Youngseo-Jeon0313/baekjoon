import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    flag=True #괜찮다.
    check=0 #0이 계속해서 같은 값만 나온다.
    STR=s[0]
    if 'R' not in s and 'B' not in s : print('YES')
    else:
        for i in range(1,n+1):
            if i==n and check==0 : break;
            if s[i]=='W' and STR!='W' and check==0: break;
            if s[i]=='W' and i!=(n-1) and s[i+1]!='W' : STR='W'; check=0
            if s[i]=='R': 
                if STR=='B': check=1;
                STR='R'
            elif s[i]=='B':
                if STR=='R': check=1;
                STR='B'
        if check==1: print('YES') #괜찮다.
        else: print('NO')


