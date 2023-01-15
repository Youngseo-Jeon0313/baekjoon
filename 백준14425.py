n, m = map(int, input().split())
a = set()
b = set()

for i in range(n):
    s = input()
    a.add(s)

for i in range(m):
    s = input()
    b.add(s)

print(len(a&b))