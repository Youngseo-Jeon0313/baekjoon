#첫번째 데이터가 정렬되어 있다고 판단하고,,
#두 번째 데이터가 앞에 있는 데이터와 비교했을 때 어떤 위치로 들어가야 하는지 판단

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): #인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break
print(array)