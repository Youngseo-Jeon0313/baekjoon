for _ in range(3):
    a,b,c,d=map(int,input().split())
    s=a+b+c+d
    if s==1: print("C")
    elif s==2: print("B")
    elif s==3: print("A")
    elif s==4: print("E")
    else: print("D")