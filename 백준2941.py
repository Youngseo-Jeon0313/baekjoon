ans=0

s=input()

index=0
while index<len(s):

    if index<len(s)-1:
        if s[index:index+3]=="dz=":ans+=1; index+=3; continue;
    temp=s[index:index+2]
    if temp in ["c=","c-","d-","lj","nj","s=","z="]:
        ans+=1; index+=2
    else: ans+=1; index+=1
    # print(index,ans)    
print(ans)

