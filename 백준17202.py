from collections import deque

A=deque(input())
B=deque(input())

List=deque([])
while len(List)<16:
    List.append(int(A.popleft()))
    List.append(int(B.popleft()))

# print(List)
while True:
    List2=[]
    
    for i in range(len(List)-1):
        List2.append((List[i]+List[i+1])%10)
    # print(List)
    # print(List2)
    List=List2
    if len(List)==2: print(List[0],List[1],sep=''); break;
