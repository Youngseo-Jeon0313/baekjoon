n=int(input())

for i in range(n):
    a=input()
    s=a[0]
    s=s.upper()

    print(s,end='')
    for i in range(1, len(a)):
        print(a[i], end='')
    print()