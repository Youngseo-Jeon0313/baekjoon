#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
#입력값은 다음과 같다.
# 5
# 1 1
# 2 3
# 3 4
# 9 8
# 5 2
#고민: 일단 입력값을 구분하는 게 일정하지 않음 주의
#힌트는 맨 위에 있는 게 갯수라는 거!
#split 못함. 이건 한 줄에 한 개씩을 할당시켜야 함.

test_case = int(input())
print(test_case)

for _ in range(test_case):
    input_data= input().split(' ')
    A=int(input_data[0])
    B=int(input_data[1])
    print(A+B)


#생각 input 받은 걸 list로 만들 수 있는가?

