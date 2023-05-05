def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a, b, n = map(int, input().split())

count = 0
for i in range(a, b+1):
    if gcd(i, n) == 1:
        count += 1

print(count)