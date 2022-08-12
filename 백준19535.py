import sys
input=sys.stdin.readline
import sys
sys.setrecursionlimit(100000)

N=int(input())
friends=[]
Tree=[0 for _ in range(N+1)]
for _ in range(N-1):
    x,y=map(int,input().split())
    friends.append([x,y])
    Tree[x]+=1
    Tree[y]+=1
G=0
for i in range(N+1):
    if Tree[i]>=3:
        G+=Tree[i]*(Tree[i]-1)*(Tree[i]-2)//6
'''
여기서 시간초과
continue로 for문을 돌리는 것이 더 시간 많이 걸림..ㅠ
어차피 트리는 모두 이어져 있으므로 node하나만 dfs 돌려도 다 간다.
'''
D=0
for friend in friends:
    D+=(Tree[friend[0]]-1)*(Tree[friend[1]]-1)


# print(G,D)
if D>3*G: print('D')
elif D<3*G: print('G')
else: print('DUDUDUNGA')
