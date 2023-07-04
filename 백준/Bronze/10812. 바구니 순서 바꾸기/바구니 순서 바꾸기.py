N,M=map(int,input().split())
List=[i for i in range(1,N+1)]
for _ in range(M):
    i,j,k=map(int,input().split())
    List_front=List[:i-1]
    temp1=List[i-1:k-1]
    temp2=List[k-1:j]
    List_back=List[j:]
    temp=List_front+temp2+temp1+List_back
    List=temp
print(*List)