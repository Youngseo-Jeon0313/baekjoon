n=int(input())

for i in range(n):
    s=list(input())
    sum=0
    for j in s:
        if j==' ':
            continue
        else:
            sum+=ord(j)-64
    if sum==100:
        print("PERFECT LIFE")
    else:
        print(sum)