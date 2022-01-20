'''
B진법 수 N을 10진법으로 바꾸어 출력하시오
A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35
'''
s='123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N,B=input().split()


ten=0
for i in range(len(N)):
    for j in range(35):
        if s[j]==N[i]:
            ten+=(j+1)*int(B)**(len(N)-i-1)

print(ten)


