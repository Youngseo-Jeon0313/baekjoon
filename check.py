def SORT(list):
    S=0;ten=1
    for i in list:
        S+=ten*i
        ten*=10
    return(S)

SORT((1,2))
from itertools import combinations as cb
n=int(input())
List=[]
if n<=55: 
    a=(cb([i for i in range(10)],2))
    L=[]
    print(len(list(a)))
    for i in a:
        L.append(SORT(i))
    L.sort()
print(L[n-10])