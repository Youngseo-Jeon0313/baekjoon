from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
arr=list(input())
score=list(map(int,input().strip().split()))



# def check(q):
#     if q[1][1]=='W':
#         index=2
#         while q[index][1]=='B':
#             index+=1
#         index+=1
#         while index<len(q)-1:
#             if q[index][1]=='B': return False 
#             index+=1
#         return True
#     if q[1][1]=='B':
#         index=2
#         while q[index][1]=='W':
#             index+=1
#         index+=1
#         while index<=len(q)-1:
#             if q[index][1]=='W': return False
#         return True
def minimize(q):
    q_=deque([])
    q_.append(q.popleft())
    # print(q_)
    while q:
        index,color=q.popleft()
        if q_[-1][1]==color : 
            #만약에 내가 뽑은 거가 똑같은 색인데 더 크면
            if (score[q_[-1][0]]<score[index] or index==n-1) and q_[-1][0]!=0:
                q_.pop()
                q_.append((index,color))
        else:
            q_.append((index,color))
    # print(q_)
    return q_




ans=0
q=deque([])
for i in range(n):
    q.append([i,arr[i]])

q=minimize(q)
N=len(q)
#정렬된 이후
# q=deque(sorted(q, key = lambda x: (-score[x[0]], -x[0])))
# print(q)
ans1=0
ans2=0
ans3=0
ans4=0
# while len(anslist)<num:
#     popthing, Color=q.popleft()
#     if popthing !=0 and popthing!=n-1:
#             anslist.append(popthing)
#             ans+=score[popthing]
# print(q)
# print((N-2)//2)
if N%2==0: num=N-1
else: num=N-2
if N==3:
    print(score[q[1][0]])
elif N%2==0:
    for i in range((N-2)//2,0,-1):
        if i%2==1:
            ans1+=score[q[num-i][0]]
            ans2+=score[q[i][0]]
        else:
            ans2+=score[q[num-i][0]]
            ans1+=score[q[i][0]]
    print(max(ans1,ans2))
else:
    for i in range((N-3)//2,0,-1):
        if i%2==1:
            ans1+=score[q[num-i][0]]
            ans2+=score[q[i][0]]
        else:
            ans2+=score[q[num-i][0]]
            ans1+=score[q[i][0]]
    for i in range(N//2,1,-1):
        if i%2==1:
            ans3+=score[q[N-i][0]]
            ans4+=score[q[i][0]]
        else:
            ans4+=score[q[N-i][0]]
            ans3+=score[q[i][0]]    
    ans2+=score[q[num][0]]
    ans4+=score[q[1][0]]
    # print('1:',ans1)
    # print('2:',ans2)
    print(max(ans1,ans2,ans3,ans4))
# print(ans1,ans2,ans3,ans4)
