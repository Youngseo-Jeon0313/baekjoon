from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
arr=list(input())
score=list(map(int,input().strip().split()))


q=deque([])
for i in range(n):
    q.append((i,arr[i]))


def greedy(q):
    q_=deque([])
    while q:
        index,color=q.popleft()
        if len(q_)>0 and q_[-1][1]==color : 
            #만약에 내가 뽑은 거가 똑같은 색인데 더 크면
            if score[q_[-1][0]]<score[index] :
                q_.pop()
                q_.append((index,color))
        else:
            q_.append((index,color))
    return q_


ans=0
ansList=[]

q=deque(q)
q=greedy(q)
if len(q)<=2: print(0); exit();
q.popleft(); q.pop();
q=sorted(q, key = lambda x: (-score[x[0]]))

N=len(q)


for i in range(N//2+N%2):
    ans+=score[q[i][0]]
print(ans)
'''

3(검) 1(흰) 2(검) 10(흰) 9(검) 3(흰) 4(검)
10를 꺼내면서 2,9를 지우지 않아도 2를 꺼내면서 점수를 얻지 못하고, 9를 꺼낼 수도 있어요!
혹시 이런 식으로 짠걸수도?..?.??..

<반례> 
3
WBW
20 1 20
'''