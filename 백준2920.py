numList=list(map(int,input().split()))
if sorted(numList, key = lambda x:x)==numList:
    print("ascending")
elif sorted(numList, key = lambda x:-x)==numList:
    print("descending")
else:
    print("mixed")