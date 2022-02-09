m,Seed,X1,X2 = map(int, input().split())
for a in range(100):
    for c in range(100):
        if X1 == (a*Seed+c) % m:
            if X2 == (a*(a*Seed+c)%m +c) %m:
                print(a,c)
                exit()