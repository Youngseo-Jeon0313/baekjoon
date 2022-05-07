'''
모든 조건들이 난잡해보이지만
Greedy임을 암시하고 있음
'''

N,K=map(int,input().split())
List=[]
for _ in range(N):List.append(list(map(int,input().split())))
Bag=[int(input()) for _ in range(K)]

