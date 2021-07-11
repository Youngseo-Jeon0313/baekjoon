a,b = input().split()
a=int(a)
b=int(b)

list_test=[]
list_test=input().split(' ')
for i in list_test:
    if int(i) < b:
        print(i, end=' ')