T=int(input())
for _ in range(T):
    n=int(input())
    x=input()
    y=input()
    flag=True
    for i in range(n):
        if x[i] =='R' and y[i]!='R': flag=False
        elif x[i] !='R' and y[i]=='R': flag=False
    if flag: print('YES')
    else: print('NO')