a = int(input()) # 0보다 크거나 같고 99보다 작거나 같은 정수가 주어짐


x=a//10
y=a%10

q=1
while True:
    i=10*y+(x+y)%10
    if i==a:
        break
    else :
        q+=1
        x=i//10
        y=i%10
        continue

print(q)