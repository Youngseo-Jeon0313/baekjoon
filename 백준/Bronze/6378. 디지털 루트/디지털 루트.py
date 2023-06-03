

while True:
    a=int(input())
    if a==0: break
    while True:
        if len(str(a))==1: break
        temp=0
        for i in str(a):
            temp+=int(i)
        a=temp
    print(a)