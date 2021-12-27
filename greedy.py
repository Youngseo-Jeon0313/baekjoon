from typing import Coroutine


n = 1260
count = 0

array = [500, 100, 50, 10]

for coin in array:
    count += n//coin #먼저 맨 처음 거슬러 줄 수 있는 종류의 '숫자'를 하나씩 더하고
    n %= coin #그 다음에 n을 coin으로 나눈 나머지로 바꿔준다.

print(count)