X,Y=map(int,input().split())
N=int(input())
List=[]
List.append(X/Y)
for _ in range(N):
    x,y=map(int,input().split())
    List.append(x/y)
List=sorted(List)
print(round(List[0]*1000,2))
