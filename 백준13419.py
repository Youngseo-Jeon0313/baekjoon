
N=int(input())
for _ in range(N):
    s=input()
    check=[0 for _ in range(len(s))]
    turn1=0
    turn2=1
    ans1=''
    ans2=''
    while True:
        if check[turn1%len(s)]:break
        else:
            ans1+=s[turn1%len(s)]
            check[turn1%len(s)]=1
            turn1=(turn1+2)%len(s)
    check=[0 for _ in range(len(s))]
    while True:    
        if check[turn2%len(s)]:break
        else:
            ans2+=s[turn2%len(s)]
            check[turn2%len(s)]=1
            turn2=(turn2+2)%len(s)

    print(ans1)
    print(ans2)