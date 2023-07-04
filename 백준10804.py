List=[i for i in range(1,21)]
for _ in range(10):
    a,b=map(int,input().split())
    temp = List[a-1:b]
    temp.reverse()
    List[a-1:b] = temp
print(*List)