List=list(map(int,input().split()))
List=sorted(List)
if List[2]>=List[0]+List[1]:
    print(List[0]+List[1]+List[0]+List[1]-1)
else:
    print(sum(List))