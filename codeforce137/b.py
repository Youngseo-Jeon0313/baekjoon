T=int(input())
for _ in range(T):
    n=int(input())
    if n<3:
        for i in range(1,n+1):
            print(i, end=' ')
        print()
    else:
        for i in range(1,n+1):
            if i==2: continue
            print(i, end=' ')
        print(2)
    