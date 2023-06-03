index=0
while True:
    a=int(input())
    if a==0: break
    index+=1
    if a%2: print("{}. odd {}".format(index, (a-1)//2))
    else: print("{}. even {}".format(index, a//2))