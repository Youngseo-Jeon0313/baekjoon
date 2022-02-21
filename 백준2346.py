from collections import deque
n=int(input())
arr=[*map(int,input().split())]
ans=[]

dq=deque()
for i in range(n):
    #해당 내용과 번째수 배열화해서 넣기
    dq.append([arr[i],i+1])

while dq:
    val=dq.popleft()
    ans.append(val[1])
    if not dq: break

    if val[0]<0:
        for i in range(-1*val[0]):
            dq.appendleft(dq.pop())
    else:
        for i in range(val[0]-1):
            dq.append(dq.popleft())
print(*ans)