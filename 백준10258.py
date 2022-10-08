T=int(input())
for _ in range(T):
    L=list(input())
    LEN=2**len(L)
    index=0
    ans=0
    flag=0
    while index<len(L):
        if L[index]=='1':
            if flag==0:
                ans+=LEN//(2**(index+1)); flag=1 #1이었다~
            else:
                flag=0
        elif L[index]=='0' and flag==1:
            ans+=LEN//(2**(index+1)); flag=1
        index+=1
        #print('야',ans)
    print(ans)