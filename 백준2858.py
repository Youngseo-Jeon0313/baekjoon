r, b = map(int,input().split())
size = r + b                       # 큰 방의 크기 (가로 * 세로)
i = 3                            # 방의 세로는 항상 3 이상
while True:                       # 답이 있는 경우만 주어지니 i가 3부터 계속 비교
    if size % i == 0:              # 직사각형이 되는 경우
        if (i - 2) * (size // i - 2) == b:    # 갈색 부분의 크기 비교
            print(max(i, size // i), min(i, size // i))
            break
    i += 1
