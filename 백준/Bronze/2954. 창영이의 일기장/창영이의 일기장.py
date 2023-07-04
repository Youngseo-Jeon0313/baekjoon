a=input()

index=0
while index<len(a):
    print(a[index], end='')
    if a[index] in ['a','e','o','i','u']:
        index+=3
    else: index+=1
print('',end=' ')
