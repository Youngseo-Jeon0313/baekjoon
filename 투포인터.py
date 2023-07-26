N, M = map(int, input().split())
nums = list(map(int, input().split()))
left, right = 0, 1
cnt = 0
while right<=N and left<=right:
    sum_nums = nums[left:right]
    total = sum(sum_nums)
    if total == M:
        cnt += 1
        right += 1
    elif total < M:
        right += 1
    else:
        left += 1

print(cnt)



'''
합이나 차의 특정 값을 구하기 위한 경우: 두 개의 포인터를 배열의 양 끝에서 시작하여 움직이면서 합이나 차를 조절하여 원하는 값을 찾습니다. 예를 들어, 주어진 합을 가지는 두 요소를 찾거나, 두 요소의 차이가 특정 값이 되는 경우 등이 있습니다.

구간 합, 평균, 최소, 최대 등을 계산하는 경우: 슬라이딩 윈도우와 함께 사용하여 구간을 유동적으로 조정하며 연산을 수행합니다. 이를 통해 시간복잡도를 줄일 수 있습니다.

두 개의 정렬된 (또는 정렬되지 않은) 배열을 병합하거나 합집합, 교집합 등을 구하는 경우에도 투포인터가 유용합니다.

'''