List=[]
for _ in range(5):
    a=int(input())
    List.append(a)
print(int(sum(List)/5))
List=sorted(List)
print(List[2])