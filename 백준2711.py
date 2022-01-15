T=int(input())

for i in range(T):
    List=list(input().split())
    List[0]=int(List[0])
    print(List[1][:List[0]-1]+List[1][List[0]:])