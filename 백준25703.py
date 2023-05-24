N=int(input())
print('int a;')
print("int *ptr = &a;")
if N>1:
    for i in range(2,N+1):
        if i==2: 
            print('int ','*'*i,'ptr',i,' = ', '&ptr',';',sep='')
        else:
            print('int ','*'*i,'ptr',i,' = ', '&ptr',i-1,';',sep='')