'''
문제에서 요구하는 형식에 맞게 짜보자
'''
import sys
input=sys.stdin.readline

import heapq
from collections import deque
N=int(input())
List=[]
heapq.heapify(List)
Graph=['' for _ in range(N+1)]
Operator=[{'parent':0,'lchild':0,'rchild':0,'val':0} for _ in range(2*N)]
SUM=0
#일단 트리를 만든다.
for j in range(1,2*N):
    temp=list(input().split())
    if len(temp)==1: 
        x=int(temp[0])
        Operator[j]['val']=x
        heapq.heappush(List,x)
        SUM+=x
    else: 
        x,y,z=temp[0], int(temp[1]),int(temp[2])
        Operator[j]['lchild']=y; Operator[y]['parent']=j
        Operator[j]['rchild']=z; Operator[z]['parent']=j
        Operator[j]['val']=x
    if j==2*N-1: Operator[j]['parent']=j
root=Operator[2*N-1]['parent']

while root!=Operator[root]['parent']:
    root=Operator[root]['parent']


q=deque([])
# if Operator[root]['val']=='+':
#     q.append([root,0]) #root가 +일 경우
# else:
#     q.append([root,1]) #root가 -일 경우


q.append([root,0]) #처음 root는 +로 초기화
minus=0
while q:
    node,operator=q.popleft()
    if 0< node and node<=N: #숫자라면
        if operator: 
            minus+=1
            #print('해당노드',node)
        continue
    q.append([Operator[node]['lchild'], operator])
    if Operator[node]['val']=='+':
        q.append([Operator[node]['rchild'],operator])
    if Operator[node]['val']=='-': #뒤집어요
        q.append([Operator[node]['rchild'],operator^1])

# print(minus)

for i in range(minus):
    x=heapq.heappop(List)
    SUM-=2*x

print(SUM)
#일단 트리를 만든다.

