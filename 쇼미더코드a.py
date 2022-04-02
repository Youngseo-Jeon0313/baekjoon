N=int(input()) #물약 개수
arr=list(map(int,input().split())) #각 물약의 가격 나열
from itertools import permutations
Sale=[[] for _ in range(N)]
for x in range(N): #각 종류별 할인 정보 제공
    pi=int(input()) #종류 몇개?
    for _ in range(pi):
        aj, dj=map(int,input().split())
        Sale[x].append((aj-1,dj))
L=list(permutations(list(range(N)),N))

def go(i,price):
    global Min
    sum=0; check=[0]*(N)
    for j in i:
        if price[j]<1: price[j]=1
        sum+=price[j]; check[j]=1
        for whichone,discount in Sale[j]:
            if not check[whichone]: price[whichone]-=discount
    if sum<Min: Min=sum
    return Min
Min=float('inf')
for i in L:
    price=tuple(arr)
    go(i,list(price))

print(Min)
