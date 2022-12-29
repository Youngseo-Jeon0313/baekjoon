List=list(map(int,input().split()))
sumList=[]

sumList.append(List[0]+List[1]+List[2])
sumList.append(List[3]+List[4]+List[5])
sumList.append(List[6]+List[7]+List[8])

sumList.append(List[0]+List[4]+List[8])
sumList.append(List[2]+List[4]+List[6])

sumList.append(List[0]+List[3]+List[6])
sumList.append(List[1]+List[4]+List[7])
sumList.append(List[2]+List[5]+List[8])

# print(set(sumList))
if len(set(sumList))==8: print("NO")
else: print("YES")
