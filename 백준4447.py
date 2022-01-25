n=int(input())

for i in range(n):
    s=input()
    b=0
    g=0
    for j in s:
        if j=='B' or j=='b':
            b+=1
        if j=='g' or j=='G':
            g+=1
    if b>g:
        print(s,'is','A BADDY')
    elif b<g:
        print(s,'is','GOOD')
    else:
        print(s,'is','NEUTRAL')