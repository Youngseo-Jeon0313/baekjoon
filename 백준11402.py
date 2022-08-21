import sys
input=sys.stdin.readline

def c(x, r):
    a = 1
    if (x < r):
        return 0
    elif (x == r):
        return 1
    for i in range(1, r + 1):
        a *= (x - i + 1)
        a //= i
    return a

n, k= map(int, input().split())
nl = []
kl = []
cnt = 0
while (n != 0 or k != 0):
    nl.append(n)
    kl.append(k)

ans = 1
for i in range(len(nl)):
    ans *= c(nl[i], kl[i])

print(ans)
