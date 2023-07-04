while True:
    a=input()
    if a=='#': break
    temp=0
    for i in a:
        if i=='1': temp+=1
    if temp%2 :
        if a[-1]=='e': 
            a=a[:-1]+'1'
        else:
            a=a[:-1]+'0'
    else:
        if a[-1]=='e': 
            a=a[:-1]+'0'
        else:
            a=a[:-1]+'1'
    print(a)