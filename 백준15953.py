t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    ans=0
    if a==0: ans+=0
    elif a==1: ans+=5000000
    elif a<=3: ans+=3000000 
    elif a<=6: ans+=2000000
    elif a<=10: ans+=500000
    elif a<=15: ans+=300000
    elif a<=21: ans+=100000
    else: ans+=0

    if b==0: ans+=0
    elif b==1: ans+=5120000 
    elif b<=3: ans+=2560000 
    elif b<=7: ans+=1280000
    elif b<=15: ans+=640000
    elif b<=31: ans+=320000
    else: ans+=0

    print(ans)