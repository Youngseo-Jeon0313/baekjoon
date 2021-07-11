#while문

answer=0
while True:
    answer=0
    a,b=input().split(' ')
    a=int(a)
    b=int(b)
    answer+=a
    answer+=b
    if answer==0:
        break
    else:
        print(a+b)
        continue