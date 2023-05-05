def find(N, X):
    s, e = 0, N-1

    while s <= e:
        m = (s + e) // 2
        v = compare(m, X)

        if v > 0:
            s = m + 1
        elif v < 0:
            e = m - 1
        else:
            return m

    return -1

# 예시
A = [3, 4, 7, 9, 23, 110]
X = 23
print(find(len(A), X))  # 4
