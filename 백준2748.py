List=[0,1]

for i in range(2,91):
    List.append(List[i-2]+List[i-1])

N=int(input())
print(List[N])