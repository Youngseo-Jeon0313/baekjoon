t=int(input())

for i in range(t):
    n=input()
    N=int(n)+int(n[::-1])
    if str(N)==str(N)[::-1]:
        print('YES')
    else:
        print("NO")