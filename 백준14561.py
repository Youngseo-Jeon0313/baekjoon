t = int(input())


val={i: str(i) for i in range(10)}
val.update({i+10: chr(65+i) for i in range(16)})



for i in range(t):
    A, n = map(int, input().split())
    ans=[]
    
    if A==0:
        print('1')
    
    else:        
        while True:
            if A==0: break
            a=A%n
            ans.append(val[a])
            A//=n

        if ans==ans[::-1]:
            print('1')
        else:
            print('0')
