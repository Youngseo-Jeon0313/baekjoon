a = int(input(),2) #2진수 입력을 10진수로 받기
b = int(input(),2)
n = 100000
mask = 2 ** n - 1
# print(type(bin(a|b))) #str
# 자리수 맞춰주기
print(bin(a&b)[2:].zfill(n))  # 십진수끼리 & 비트연산자하면 연산결과후의 십진수를 출력하는데 그걸 이진수로 바꿔줌
print(bin(a|b)[2:].zfill(n))
print(bin(a^b)[2:].zfill(n))
print(bin(a^mask)[2:].zfill(n))
print(bin(b^mask)[2:].zfill(n))