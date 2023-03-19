T=int(input())
for _ in range(T):
    ascii_list=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    Dict={}
    n=int(input())
    s=input()
    before='0' #방금 전에 뺀 거?
    add=['0']
    for i in s:
        if len(add)==0: add=[i]; continue
        if add[0]==i and add[1]!=i: n-=1
        add=list(add[-1]+i)
        print(str(add))
        if str(add) in Dict.keys(): 
            n-=1          
        else: 
            Dict[str(add)]=1
        
    print(n-1)