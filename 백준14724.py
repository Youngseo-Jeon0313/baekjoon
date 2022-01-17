DONG = {"PROBRAIN":0, "GROW":0,"ARGOS":0, "ADMIN":0,"ANT":0,"MOTION":0,"SPG":0,"COMON":0,"ALMIGHTY":0}

n=int(input())

for i in range(9):
    L=0
    S=list(map(int, input().split()))
    for j in S:
        if j>L:
            L=j
    if L>=0:
        DONG[i]=L

max_key = max(DONG, key=DONG.get)


print(list(DONG.keys())[max_key])
