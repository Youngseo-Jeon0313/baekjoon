while True:
    a=list(input().split())
    if a[0]=='#':
        break
    for i in a:
        j=i[::-1]
        print(j,end=' ')
    print()