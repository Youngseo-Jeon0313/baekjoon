#1차원 배열  --  최대 최소

a=int(input())


b=(input().split(' ')) #이렇게 하면 list로 저장되는 구나..

for i in range(a):
    b[i] = int(b[i])

print(b)

max = b[0]
for i in range(a):
    if b[i] > max:
        max=b[i]


min = b[0]
for i in range(a):

    if b[i] < min:
        min = b[i]


print(min, max)



#실수 주의 미리 해놓는 max = 어떤 것 이게 for문 안에 들어가면 안됐음 ㅠㅠ
