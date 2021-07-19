#점수 조작하기

a=int(input())

b=input().split(' ')

for i in range(a):
    b[i]=int(b[i])

max=b[0]
for i in range(a):
    if b[i] > max:
        max=b[i]

x=0
for i in range(a):
    b[i]=b[i]/max*100
    x+=b[i]

print(x/a)

