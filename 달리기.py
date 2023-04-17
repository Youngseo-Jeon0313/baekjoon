n = int(input())
rank = list(map(int, input().split()))

result = [0] * n
result[-1] = 1  # 마지막 사람은 무조건 1등이므로 초기화

for i in range(n - 2, -1, -1):  # 뒤에서부터 각 사람의 최고 등수 계산
    if rank[i] > rank[i + 1]:
        result[i] = result[i + 1] + 1
    else:
        j = i + 1
        while j < n and rank[i] <= rank[j]:
            j = j + result[j]
        result[i] = j - i

for r in result:
    print(r, end=' ')
