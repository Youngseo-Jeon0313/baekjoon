while True:
    arr=['-','\\','(','@','?','>','&','%','/']
    a=input()
    ans=0
    if a=='#': break
    for i in range(len(a)):
        Index=arr.index(a[i])
        if Index==8: Index=-1
        ans+=(8**(len(a)-i-1)*Index)
    print(ans)