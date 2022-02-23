a, b = input().split()

MIN=1000
for i in range(len(b) - len(a) + 1):
    count = 0
    for j in range(len(a)):
        if a[j] != b[i + j]:
            count += 1
    if count<MIN: MIN=count

print(MIN)