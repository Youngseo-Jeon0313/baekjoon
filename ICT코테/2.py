def numDuplicates(name, price, weight):
    ans=0
    List=[]
    LEN=len(name)
    for i in range(LEN):
        List.append([name[i],price[i],weight[i]])
    List=sorted(List,key=lambda x:[x[0],x[1],x[2]])
    List.append(['0','0','0']);
    # print(List)
    first=0; second=0; third=0; num=0
    for i in List:
        if i[0]==first and i[1]==second and i[2]==third:
            num+=1
        else:
            if num>1: ans+=num-1
            num=1; first=i[0]; second=i[1]; third=i[2]
    return ans

print(numDuplicates(["ball","bat","glove","glove","glove"],[2,3,1,2,1],[2,5,1,1,1]))
print(numDuplicates(["ball",'box','ball','ball','box'],[2,2,2,2,2],[1,2,1,1,3]))
print(numDuplicates(["box",'box','box','box'],[2,2,2,2],[2,2,2,2]))