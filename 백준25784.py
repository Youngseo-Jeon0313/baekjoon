a,b,c=map(int,input().split())
List=sorted([a,b,c])
if List[0]+List[1]==List[2]: print(1)
elif List[0]*List[1]==List[2]: print(2)
else: print(3)