iter=int(input())


for i in range(iter):
    N=int(input())

    myList =list()

    myList.append(1)
    myList.append(1)
    myList.append(1)
    myList.append(2)
    myList.append(2)



    for i in range(5,N+1):
        a=myList[i-5]+myList[i-1]
        myList.append(a)


    print(myList[N-1])

