array = [7,5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i #일단 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]: #매번 가장 앞쪽 위치를 i라고 하고 가장 작은 원소를 쭈우욱쭉 찾음
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] #스와프

print(array)