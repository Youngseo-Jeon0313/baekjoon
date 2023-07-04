N=int(input())
List=[]
for _ in range(N):
    a,b=input().split()
    b=int(b)
    List.append([b,a])
List=sorted(List)
print(List[0][1])