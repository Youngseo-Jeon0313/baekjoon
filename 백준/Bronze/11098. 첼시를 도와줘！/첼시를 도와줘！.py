T=int(input())
for _ in range(T):
    M=0; Player=''
    n=int(input())
    for _ in range(n):
        a,b=input().split()
        a=int(a)
        if a>M: Player=b; M=a
    print(Player)
