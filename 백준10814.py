List=[]

n=int(input())
for _ in range(n):
    age,name=input().split()
    age=int(age)
    List.append([age,name])
List=sorted(List,key= lambda x:(x[0]))

for i in  List:
    print(*i)