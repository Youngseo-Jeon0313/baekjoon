import sys
input=sys.stdin.readline

s,n=input().split()
s=int(s)
for k in n:
    if k=='1' or k=='4' :
        print(' '*(s+2),end='',sep='')
    else:
        print(' ',end='',sep='')
        print('-'*s,end='',sep='')
        print(' ',end='',sep='')
    print(' ',end='',sep='')
print()
i=0
for j in range(s):
    for i in n:
        if i=='5' or i=='6':
            print('|',' '*s,' ',end='',sep='')
        elif i=='1' or i=='2' or i=='3' or i=='7':
            print(' ',' '*s,'|',end='',sep='')
        else:
            print('|',' '*s,'|',end='',sep='')
        print(' ',end='',sep='')
    print()
for k in n:
    if k=='1' or k=='0' or k=='7':
        print(' '*(s+2),end='',sep='')
    else:
        print(' ',end='',sep='')
        print('-'*s,end='',sep='')
        print(' ',end='',sep='')
    print(' ',end='',sep='')
print()
for j in range(s):
    for i in n:
        if i=='2':
            print('|',' '*s,' ',end='',sep='')
        elif i=='1' or i=='3' or i=='4' or i=='5' or i=='7' or i=='9':
            print(' ',' '*s,'|',end='',sep='')
        else:
            print('|',' '*s,'|',end='',sep='')
        print(' ',end='',sep='')
    print()
for k in n:
    if k=='1' or k=='4' or k=='7':
        print(' '*(s+2),end='',sep='')
    else:
        print(' ',end='',sep='')
        print('-'*s,end='',sep='')
        print(' ',end='',sep='')
    print(' ',end='',sep='')
print()