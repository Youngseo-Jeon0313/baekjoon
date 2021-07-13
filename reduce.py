#reduce함수
#reduce(함수, 시퀀스)
#시퀀스(문자열, 리스트, 튜플)의 원소들을 누적적으로 함수에 적용시킴

from functools import reduce

a = reduce(lambda x, y : x+y, [0,1,2,3,4])
print(a)

print(reduce(lambda x, y: y + x, 'abcde'))
#'edcba' 왜? y+x를 했으니까 b에 a를 더하고, ... 이런 작업 반복


