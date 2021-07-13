#filter(함수, 리스트)
#걸러주기! 리스트에 있는 원소들을 함수에 적용시켜서 결과가 참인 값들로 새로운 리스트를 만들어주는 작업!


print(list(filter(lambda x: x<5, range(10))))

