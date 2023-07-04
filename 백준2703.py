T=int(input())
for _ in range(T):
    a=input()
    b=list(input())
    for i in a:
        if i==' ': print(' ',end='')
        else:
            print(b[ord(i)-ord('A')],end='')
    print()
