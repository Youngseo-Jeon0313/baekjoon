List=[]
N=int(input())
for _ in range(N):
    List.append(list(map(int,input().split())))
List=sorted(List,key = lambda x:[x[1], x[0]])
for i in List:
    print(*i)