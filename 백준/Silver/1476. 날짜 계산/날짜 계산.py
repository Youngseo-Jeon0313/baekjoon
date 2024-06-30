E, S, M = map(int,input().split())
E%=15; S%=28; M%=19
# print(5266//15, 5266%15)
# print(5266//28, 5266%28)
# print(5266//19, 5266%19)
for i in range(1,100000):
    if i%15 == E and i%28 == S and i%19 == M:
        print(i)
        break
