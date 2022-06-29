from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
arr=list(input())
score=list(map(int,input().strip().split()))


ans=0
q=deque([])
for i in range(n):
    q.append((i,arr[i]))

q_=deque([])
q_.append(q.popleft())
while q:
    index,color=q.popleft()
    if q_[-1][1]==color : 
        #만약에 내가 뽑은 거가 똑같은 색인데 더 크면
        if score[q_[-1][0]]<score[index] or index==n-1 or q_[-1][0]!=0:
            q_.pop()
            q_.append((index,color))
    else:
        q_.append((index,color))

N=len(q_)

ans=0
ansList=[]
q=sorted(q_, key = lambda x: -score[x[0]])
q=deque(q)

popthing,Color=q.popleft()
ansList.append(popthing)
ans+=score[popthing]

while len(ansList)<(N-2)//2+N%2 and q:
    popthing, Color = q.popleft()
    if popthing != 0 and popthing !=n-1 and popthing+1 not in ansList and popthing-1 not in ansList:
        #여기서 시간초과를 당하는 것 같다ㅠㅠㅠㅠ
        ansList.append(popthing)
        ans+=score[popthing]
print(ans)
            
