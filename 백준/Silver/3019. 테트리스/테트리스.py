C,P=map(int,input().split())
List=list(map(int,input().split()))
ans=0
if P==1:
    for j in range(C):
        if List[j]>-1: ans+=1
        a=List[j]
        if j+3<C and List[j+1]==a and List[j+2]==a and List[j+3]==a: ans+=1
elif P==2:
        for j in range(C):
            a=List[j]
            if j+1<C and List[j+1]==a: ans+=1
elif P==3:
        for j in range(C):
            a=List[j]
            if j+2<C and List[j+1]==a and List[j+2]==a+1: ans+=1
            if j+1<C and List[j+1]==a-1: ans+=1
elif P==4:
        for j in range(C):
            a=List[j]
            if j+2<C and List[j+1]==a-1 and List[j+2]==a-1: ans+=1
            if j+1<C and List[j+1]==a+1: ans+=1
elif P==5:
        for j in range(C):
            a=List[j]
            if j+2<C and List[j+1]==a-1 and List[j+2]==a : ans+=1
            if j+2<C and List[j+1]==a and List[j+2]==a: ans+=1
            if j+1<C and List[j+1]==a-1: ans+=1
            if j+1<C and List[j+1]==a+1: ans+=1
elif P==6:
    for j in range(C):
            a=List[j]
            if j+2<C and List[j+1]==a and List[j+2]==a : ans+=1            
            if j+1<C and List[j+1]==a: ans+=1
            if j+1<C and List[j+1]==a-2: ans+=1
            if j+2<C and List[j+1]==a+1 and List[j+2]==a+1: ans+=1            

else:
      for j in range(C):
            a=List[j]
            if j+2<C and List[j+1]==a and List[j+2]==a : ans+=1
            if j+1<C and List[j+1]==a: ans+=1
            if j+1<C and List[j+1]==a+2: ans+=1
            if j+2<C and List[j+1]==a and List[j+2]==a-1: ans+=1            

print(ans)
