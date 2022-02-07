'''
sum=0
N=int(input())
N-=1
i=1
while True:
    while (N-i)>=0:
        N-=i
        i+=1
    sum+=3**(i-1)
    if N>0:
        sum+=3**(N-1)
    print(i,N)
'''
#개수가 1,2,4,8,16 ...이렇게 감
n = int(input())
s = []
num = 0
#2진수로 바꾸기
while n > 0:
    s.append(n % 2)
    n //= 2
#2진수로 바꾼 거를 다시 3진수로 바꾸기
for i in range(len(s)):
    if s[i] == 1:
        num += 3 ** i
print(num)