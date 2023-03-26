x, n = map(int, input().split())

def f(t, num):
    if num == 4:
        return 4
    elif num == 8:
        return [8, 2, 7][t % 3]
    elif num == 0:
        return [0, 6, 5, 12][t % 4]
    else:
        if t == 0:
            return num
        else:
            if num % 2 == 0:
                return f(t - 1, num // 2 ^ 6)
            else:
                return f(t - 1, num * 2 ^ 6)

print(f(n, x))