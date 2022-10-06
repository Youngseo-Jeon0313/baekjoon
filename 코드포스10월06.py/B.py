T=int(input())
for _ in range(T):
    n=int(input())
    for i in range(n):
        if i==0:
            print('1')
        elif i==1:
            print('1 1')
        else:
            print('1 ','0 '*(i-1),'1',sep='')
    