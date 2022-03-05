
def SORT(L):
    S=0;ten=1
    for i in L:
        S+=ten*i
        ten*=10
    return(S)

from itertools import combinations as cb
n=int(input())
L=[]
if n<10:
    print(n)
elif n<55: 
    a=(cb([i for i in range(10)],2))
    for i in a: L.append(SORT(i)); L.sort()
    print(L[n-10])
elif n<175: 
    a=(cb([i for i in range(10)],3))
    for i in a: L.append(SORT(i));L.sort()
    print(L[n-55])
elif n<385: 
    a=(cb([i for i in range(10)],4))
    for i in a: L.append(SORT(i));L.sort()
    print(L[n-175])
elif n<637: 
    a=(cb([i for i in range(10)],5))
    for i in a: L.append(SORT(i));L.sort()
    print(L[n-385])
elif n<847: 
    a=(cb([i for i in range(10)],6))
    for i in a: L.append(SORT(i));L.sort()
    print(L[n-637])
elif n<967: 
    a=(cb([i for i in range(10)],7))
    for i in a: L.append(SORT(i));L.sort()
    print(L[n-847])
elif n<1012: 
    a=(cb([i for i in range(10)],8))
    for i in a: L.append(SORT(i));L.sort()
    print(L[n-967])
elif n<1022: 
    a=(cb([i for i in range(10)],9))
    for i in a: L.append(SORT(i));L.sort()
    print(L[n-1012])
elif n<1023: 
    a=(cb([i for i in range(10)],10))
    for i in a: L.append(SORT(i));L.sort()
    print(L[n-1022])
else: print(-1)

'''

ans = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in ans:
    for j in range(i % 10):
        ans.append(i * 10 + j)
ans = sorted(ans)
num = int(input())
if num >= len(ans):
    print(-1)
else:
    print(ans[num])
    '''