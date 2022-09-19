import sys
input=sys.stdin.readline

N=int(input())
Dict={}#자식: 부모
def find(target,check):
    # print('야호',target,check)
    if target==check: return 1
    elif target not in Dict.keys(): return 0
    else: 
        for i in Dict[target]:
            if find(i,check): return 1

for _ in range(N-1):
    x,y=input().split()
    if y in Dict.keys():
        Dict[y]+=[x]
    else:
        Dict[y]=[x]
# print(Dict)
one,two=input().split()
if find(two,one):print(1)
elif find(one,two): print(1)
else: print(0)

'''
6
A B
B C
B D
D E
A D
B E
1



'''