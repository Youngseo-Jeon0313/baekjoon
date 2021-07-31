a = int(input())


for i in range(a):
    num=0
    score=0
    aver=0
    b = input().split(' ')
    for i in range(1,len(b)):
        score+=int(b[i])
    aver+=score/int(b[0])
    for i in range(1,len(b)):
        if int(b[i]) > aver:
            num+=1
    print("{:.3f}%".format(num/int(b[0])*100))
