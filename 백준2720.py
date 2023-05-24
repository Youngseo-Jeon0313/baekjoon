T=int(input())
for _ in range(T):
    money=int(input())
    a=money//25
    money%=25
    b=money//10
    money%=10
    c=money//5
    money%=5
    d=money
    print(a,b,c,d)