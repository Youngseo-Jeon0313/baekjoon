def jinsu(n, m):
    s = 0
    while True:
        if n // m == 0:
            s += n
            break
        s += n%m
        n = n // m
    return s


for i in range(1000,10000):
    if jinsu(i,10) == jinsu(i,12) and jinsu(i,10) == jinsu(i,16): print(i)
