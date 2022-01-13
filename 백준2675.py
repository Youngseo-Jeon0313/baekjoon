n=int(input())

for i in range(n):
    s,t= input().split()
    for i in range(len(t)):
        print(t[i]*int(s), end='')
    print()