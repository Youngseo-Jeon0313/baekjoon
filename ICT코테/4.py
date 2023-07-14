
def programmerStrings(s):
    first=0; second=len(s)-1
    #p r o g a m e
    List=[1,3,1,1,1,2,1]
    index=0
    for i in s:
        index+=1
        if i=='p' and List[0]>0: List[0]-=1; 
        elif i=='r' and List[1]>0: List[1]-=1; 
        elif i=='o' and List[2]>0: List[2]-=1; 
        elif i=='g' and List[3]>0: List[3]-=1; 
        elif i=='a' and List[4]>0: List[4]-=1; 
        elif i=='m' and List[5]>0: List[5]-=1; 
        elif i=='e' and List[6]>0: List[6]-=1; 
        if List==[0,0,0,0,0,0,0]:  #끝났다.
            first=index; break;
    List=[1,3,1,1,1,2,1]
    for j in range(second,-1,-1):
        if s[j]=='p' and List[0]>0: List[0]-=1; 
        elif s[j]=='r' and List[1]>0: List[1]-=1; 
        elif s[j]=='o' and List[2]>0: List[2]-=1; 
        elif s[j]=='g' and List[3]>0: List[3]-=1; 
        elif s[j]=='a' and List[4]>0: List[4]-=1; 
        elif s[j]=='m' and List[5]>0: List[5]-=1; 
        elif s[j]=='e' and List[6]>0: List[6]-=1; 
        if List==[0,0,0,0,0,0,0]:  #끝났다.
            second=j; break;
        # print(List)
    # print(first,second)
    return second-first

print(programmerStrings('programmerprogrammer'))
print(programmerStrings('progxrammerrxproxgrammer'))


