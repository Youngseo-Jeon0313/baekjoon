while True:
    a=int(input())
    if a==0: break
    print(a,end=' ')
    while len(str(a))>1:
        temp=1
        for i in str(a):
            temp*=int(i)
        print(temp,end=' ')
        a=temp
    print()
