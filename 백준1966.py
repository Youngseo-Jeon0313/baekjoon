from collections import deque


t=int(input())
for i in range(t):
    N,M=map(int, input().split())
    List=deque(map(int,input().split()))
    for i in range(len(List)):
        for j in List:
            flag=True
            if List[i]<j:
                x=List.popleft()
                List.append(x)
                flag=False
                continue
            if flag==True:
                break
            
    print(List)

    

