def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end) //2
    #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    if array[mid] ==target:
        return mid
    #중간값의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, mid+1, end)

n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result +1)

#logN에 해결해야 할 때 사용


#파이썬 이진 탐색 라이브러리
#bisect_left(a,x):정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
#bisect_right(a,x):정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환

#생각. 값이 특정 범위에 속하는 데이터 개수 구하기?
#값이 4인 데이터 개수 출력
#print(count_by_range(a,4,4)) -이때 a는 배열!

def binary_search(target, data):
    data.sort()
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid # 함수를 끝내버린다.
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return None
