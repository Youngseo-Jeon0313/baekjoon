numList=[]

for _ in range(5):
    a=int(input())
    if a<40: numList.append(40)
    else: numList.append(a)

print(sum(numList)//5)