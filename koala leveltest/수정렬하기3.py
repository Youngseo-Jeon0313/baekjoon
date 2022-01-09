'''
메모리초과 문제
왜냐?? 33이렇게 두 번 들어갈 때 문제가 생기기 때문.
'''

N=int(input())
myList=list()

for i in range(N):
    myList.append(int(input()))

myList.sort()

for j in myList:
    print (j)