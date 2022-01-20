t=int(input())

for i in range(t):
    s=int(input())
    flag=False

    for j in range(2,65):
        val=[]
        x=s
        while True:
            if x==0: break
            val.append(x%j)
            x//=j
        is_palindrome = True
        for k in range(len(val)//2):
            if val[k] != val[-1-k]:
                is_palindrome = False
        if is_palindrome == True:
            flag =True
    
    if flag == True: print(1)
    else: print(0)