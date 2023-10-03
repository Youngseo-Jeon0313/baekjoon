from collections import deque
N=int(input())
List=[]
for _ in range(N):
   List.append(list(input().split()))
print(List)
deq = deque([[List[0][0],0,0,'']]) #값, x좌표, y좌표, 전값
max_ans=0
min_ans=10**6
while deq:
  value, x, y, before_value = deq.popleft()
  if x==N-1 and y==N-1: 
     value=int(value); 
     print(value)
     max_ans=max(max_ans,value)
     min_ans=min(min_ans,value)
     continue
  value=str(value); before_value=str(before_value)
  if (x+y)%2==0: #숫자임
    if x+1<=N-1:
       deq.append([List[x+1][y],x+1,y,eval(before_value+value)])
    if y+1<=N-1:
       deq.append([List[x][y+1],x,y+1,eval(before_value+value)])
  else: #기호
    if x+1<=N-1:
        deq.append([List[x+1][y],x+1,y,before_value+value])
    if y+1<=N-1:
        deq.append([List[x][y+1],x,y+1,before_value+value])

print(max_ans, min_ans)