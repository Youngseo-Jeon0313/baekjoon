while True:
    a,b,c=map(int,input().split())
    if a==0 and b==0 and c==0: break;
    List=[a,b,c]
    List=sorted(List)
    if List[2]**2==List[1]**2+List[0]**2: print("right")
    else: print("wrong")
    