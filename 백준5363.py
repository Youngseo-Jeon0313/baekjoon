N=int(input())
for i in range(N):
    a = list(input().split(' '))
    a.append(a[0])
    a.append(a[1])
    a.pop(0)
    a.pop(0)
    for i in a:
        print(i, end=' ')
    print()

    