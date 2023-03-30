List=[0,1]
for i in range(1000):
    List.append(List[-1]+List[-2])
N=int(input())
print(List[N+1]%10007)