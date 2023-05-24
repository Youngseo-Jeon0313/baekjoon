t=int(input())
for _ in range(t):
    List=[]
    n=int(input())
    a=bin(n)[2::]
    a=str(a)
    for i in range(len(a)):
        if a[i]=='1':
            List.append(len(a)-i-1)
    print(*sorted(List))
