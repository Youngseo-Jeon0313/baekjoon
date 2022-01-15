T=int(input())

for i in range(T):
    car=int(input())
    n=int(input())
    for i in range(n):
        s, price=map(int, input().split())
        car+=s*price

    print(car)