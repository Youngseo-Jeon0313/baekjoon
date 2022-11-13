t=int(input())

for _ in range(t):
    n=int(input())
    List=list(map(int,input().split()))
    flag=True
    for i in List:
        if i%2==0: print('Alice'); flag=False; break;
    if flag: print("Bob")