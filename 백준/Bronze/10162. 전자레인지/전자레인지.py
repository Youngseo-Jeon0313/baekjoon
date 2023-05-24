t=int(input())
a=t//300
b=t%300//60
c=t%300%60//10
d=t%300%60%10
if d: print(-1)
else:
    print(a,b,c)