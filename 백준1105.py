L, R = input().split()

if len(L)==len(R) :
    answer = 0
    for i in range(len(L)):
        if L[i]==R[i] and L[i]=='8': 
            answer+=1
        elif L[i]==R[i] and L[i]!='8':
            continue
        else: 
            break; 
    print(answer)
else: 
    print(0)