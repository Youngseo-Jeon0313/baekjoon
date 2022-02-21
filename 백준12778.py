t=int(input())
for i in range(t):
    num, method=input().split()
    if method=='N':#숫자를 문자로
        arr=list(map(int,input().split()))
        for i in arr:
            print(chr(i+64),end=' ')
        print()
    else:
        arr=list(input().split())
        for i in arr:
            print(ord(i)-64, end=' ')
        print()
