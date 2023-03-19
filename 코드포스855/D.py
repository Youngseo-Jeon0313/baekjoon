T=int(input())
for _ in range(T):
    ascii_list=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    n=int(input())
    n-=1
    s=input()
    s+='1'
    
    before='1'
    count=0
    add=['0']
    for i in s:
        # print(i,n)
        if before==i: 
            count+=1
        else:    
            if count>2:
                n-=(count-2)
            count=1
            before=i
        if len(add)==0: add=[i]; continue
        if add[0]==i and add[1]!=i: n-=1
        add=list(add[-1]+i)
    print(n)