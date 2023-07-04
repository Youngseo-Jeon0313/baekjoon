while True:
    a=int(input())
    if a==0: break
    else:
        while len(str(a))>=2:
            temp=0
            for i in str(a):
                temp+=int(i)
            a=temp
    print(a)