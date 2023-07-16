from collections import deque
N=int(input())

List=[i for i in range(1,N+1)]
List=deque(List)
index=1
while len(List)>1:
    turn = index**3
    turn = (turn)%len(List)
    where = turn
    if turn==0: List.pop()
    else: 
        for _ in range(turn-1):
            a=List.popleft()
            List.append(a)
        List.popleft()
    # print(List)
    index+=1
    

print(*List)