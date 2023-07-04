while True:
    a=input()
    if a=='#': break
    ans=0
    for i in range(len(a)):
        if a[i]==' ': continue
        ans+=(i+1)*(ord(a[i])-ord('A')+1)
    print(ans)