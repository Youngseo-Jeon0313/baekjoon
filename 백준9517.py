time=210
num=int(input())
questions=int(input())

while True:
    a,b=input().split()
    if b=='T': 
        if time-int(a)>0:
            num=(num%8+1)
        time-=int(a)
    else:
        time-=int(a)
    if time<=0: break
print(num)
