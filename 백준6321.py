n=int(input())
for z in range(n):
    a=input()
    print('String ','#',z+1,sep='')
    for i in a:
        temp=(ord(i)+1)
        if temp==91: temp='A'
        else: temp=chr(temp)
        print(temp,end='')
    print()
    print()