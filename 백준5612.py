n = int(input())
m = int(input())
max_p = m
for _ in range(n):
    a, b = map(int, input().split())
    m = m+a-b
    if m < 0:
        max_p = 0
        break
    max_p=max(max_p, m)
print(max_p)