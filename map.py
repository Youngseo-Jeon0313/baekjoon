#map(함수, 리스트)
#map 함수는 함수와 리스트를 인자로 받는다. 그리고 리스트로부터 원소들을
#하나씩 꺼내서 함수를 적용시킨 다음, 그 결과를 새로운 리스트에 담아준다.

#map??
#map 함수란 반복가능한 iterable 객체를 받아서 각 요소에 함수를 적용해주는 함수
#map(적용시킬 함수, 적용할 요소들)

def add_1(n):
    return n + 1

target = [1,2,3,4,5]


# result = []
# for value in target:
#     result.append(add_1(value))

# print(result)

result = map(add_1, target)
result = list(result)
map(str, result)

print(result)




map(lambda x: x**2, range(5))
a = list(map(lambda x: x**2, range(5)))
print(a)

