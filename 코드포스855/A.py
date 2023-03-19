from collections import deque

T=int(input())
for _ in range(T):
    n=int(input())
    String=input()
    String=deque(String)
    M=0; E=0; O=0; W=0;
    flag=True
    while String:
        judge=String.popleft();
        # print(judge, flag)
        if judge=="M" or judge=='m':
            if E>0 or O>0 or W>0: flag=False; break;
            M+=1
        elif judge=="E" or judge=='e':
            if M==0: flag=False; break;
            if O>0 or W>0: flag=False; break;
            E+=1
        elif judge=="O" or judge=='o':
            if M==0 or E==0: flag=False; break;
            if W>0: flag=False; break;
            O+=1
        elif judge=="W" or judge=='w':
            if M==0 or E==0 or O==0: flag=False; break;
            W+=1
        else:
            flag=False
            break;    
    if M*E*O*W==0: flag=False
    if flag: print("YES")
    else: print("NO")