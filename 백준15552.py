#input 대신 sys.stdin.readline()을 사용하는 이유?
#한 두줄 입력받는 문제들과 다르게, 반복문으로 여러줄을 입력받아야 할 때는
#input()으로 입력받는다면 시간초과가 발생할 수 있기 때문!

import sys

a=sys.stdin.readline()

for _ in range(int(a)): #주의 range로 감싸는 거!
    input_data=sys.stdin.readline().split(' ') #다섯 번을 다 돌려면 한 번 split 한 결과를 list에 담아야 함!
    x=input_data[0]
    y=input_data[1]
    print(int(x)+int(y))