N=int(input())
bird=N
i=1
time=0
while bird:
    bird-=i
    if bird<i+1: i=1
    else: i+=1
    time+=1

print(time)