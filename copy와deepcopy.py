import copy

# 원본 리스트와 내부 리스트 생성
original_list = [1, 2, 3, [4, 5]]

# 얕은 복사 (shallow copy)
shallow_copied_list = copy.copy(original_list)

# 깊은 복사 (deep copy)
deep_copied_list = copy.deepcopy(original_list)

# 원본 리스트의 내부 리스트를 변경
original_list[3][0] = 99

# 결과 출력
print("Original List:", original_list)
print("Shallow Copied List:", shallow_copied_list)
print("Deep Copied List:", deep_copied_list)

'''
Original List: [1, 2, 3, [99, 5]]
Shallow Copied List: [1, 2, 3, [99, 5]]
Deep Copied List: [1, 2, 3, [4, 5]]
'''