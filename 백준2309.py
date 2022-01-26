from itertools import combinations as cb
L=list()
'''
어떤 우연한 기회에 다 합해서 100이 될 수 있음
조합으로 뽑았을 때 합해서 100이 되는 경우를 구하면 된다.
'''
for i in range(9):
    L.append(int(input()))

for t in cb(L,7):
    if sum(t)==100:
        t=list(t)
        t.sort()
        for i in range(7):
            print(t[i])
        break