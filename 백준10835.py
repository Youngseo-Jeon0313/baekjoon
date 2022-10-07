from collections import deque

N = int(input())
left = deque(list(map(int, input().split())))
right = deque(list(map(int, input().split())))

ans = 0
while left and right:
    if left[0] > right[0]:
        ans += right[0]
        right.popleft()
    else:
        leftMAX = max(left)
        if leftMAX <= right[0]:
            left.popleft()
            right.popleft()
        else:
            while left and left[0] != leftMAX:
                left.popleft()


print(ans)