from math import sqrt,floor

# 소수 판별 함수(2이상의 자연수에 대하여)
def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, floor(sqrt(x))+1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

D={'0':'0','1':'1','2':'2','5':'5','6':'9','8':'8','9':'6'}

N=input()
if N=='1': print("no")
else:
    M=''
    flag=True
    for i in N:
        if i in D.keys():
            M+=D[i]
        else:
            flag=False
    M=M[::-1]
    if flag:
        if is_prime_number(int(N)) and is_prime_number(int(M)):
            print("yes")
        else:
            print("no")
    else:
        print("no")