import sys
input=sys.stdin.readline

numList=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27]
i=28
while len(numList)<1000000:
    check=[0 for _ in range(10)]
    flag=True
    for j in str(i):
        j=int(j)
        if check[j]: 
            flag=False; 
        else:
            check[j]=1
    if flag: numList.append(i)
    i+=1

while True:
    n=int(input())
    if n==0: break
    print(numList[n-1])