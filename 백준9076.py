T=int(input())
for _ in range(T):
    List=list(map(int,input().split()))
    temp=sum(List)
    List=sorted(List)
    if List[1]+4<=List[-2]: print("KIN")
    else: 
        temp-=(List[0]+List[-1])
        print(temp)
    