myList= list()

while True:
    a = int(input())
    if a == 0:
        break
    else:
        myList.append(a)


for i in myList:
    if str(i) == str(i)[::-1]:
        print('yes')
    else:
        print('no')