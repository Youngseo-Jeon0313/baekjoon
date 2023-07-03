t=int(input())

for _ in range(t):
    n = int(input())
    time = 0
    while (time+1) + (time+1)**2 <= n:
        time += 1
    print(time)