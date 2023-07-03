temp=0
flag=False
while True:
    a=float(input())
    if a==999: break
    if not flag: 
        flag=True; temp=a
    else:
        print("{:.2f}".format(a-temp))
        temp=a
