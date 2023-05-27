while True:
    a=input()
    if a=='0': break
    ans=0
    ans+=len(a)-1
    ans+=2
    for i in a:
        if i=='0': ans+=4
        elif i=='1': ans+=2
        else: ans+=3
    print(ans)