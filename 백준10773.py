N=int(input())
PLAY=list()
for i in range(N):
    a=int(input())
    if a ==0:
        PLAY.pop()
    else:
        PLAY.append(a)

sum=0
for i in PLAY:
    sum+=i

print(sum)