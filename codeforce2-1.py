#굳이 일일이 써보면
#2,3,4,5,6,8,9,10,11(3+3+3+2),12(3+3+3+3),13(3+3+3+2+2),14(3+3+3+3+2)
#안돼 7(3+2+2),
t=int(input())
for _ in range(t):
    s=input()
    STR=s[0]
    sum=1
    flag=True
    if len(s)==1: flag=False;
    else:
        for i in range(1,len(s)):
            if i==len(s)-1:
                if s[i]!=STR: flag=False; break;
                elif s[i]==STR:
                    sum+=1
                    if sum!=1: continue;
                    else: flag=False; break;
            elif s[i]==STR: sum+=1;
            elif s[i]!=STR:
                if sum!=1: sum=1; STR=s[i]
                else: flag=False; break;
    if flag==False: print('NO')
    else: print('YES')