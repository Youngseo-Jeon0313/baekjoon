a,b,c=map(int,input().split())
List=[a,b,c]
List=sorted(List)
if List[1]-List[0]<List[2]-List[1]:
    print((List[2]+List[1])//2)
elif List[1]-List[0]>List[2]-List[1]:
    print((List[0]+List[1])//2)
else: print(List[2]+List[2]-List[1])