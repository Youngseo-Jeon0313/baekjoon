import sys



T=int(input())
for i in range(T):
    ascii_list=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    Upper={}
    Lower={}
    for i in ascii_list: Upper[i]=0; Lower[i]=0
    A, B=map(int,input().split())
    Str=input()
    for i in range(A):
        if Str[i].isupper(): 
            if Str[i] in Upper.keys():
                Upper[Str[i]]+=1
            else:
                Upper[Str[i]]=1
        else:
            if Str[i].upper() in Lower.keys():
                Lower[Str[i].upper()]+=1
            else:
                Lower[Str[i].upper()]=1
    ans=0
    ascii_list=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for a in ascii_list:
        if a in Upper.keys() or a in Lower.keys():
            Up=Upper[a]; Low=Lower[a]
            # print(a,Up,Low)
            ans+=min(Up,Low)
            temp=max(Up,Low)-min(Up,Low)
            if temp>=2:
                if temp//2<=B:
                    B-=temp//2
                    ans+=temp//2
                else:
                    ans+=B
                    B=0

    print(ans)