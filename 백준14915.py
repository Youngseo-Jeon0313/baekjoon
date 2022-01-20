val={i: str(i) for i in range(10)}
val.update({i+10: chr(65+i) for i in range(16)})


m, n = map(int,input().split())
ans=[]

if m==0:
    print ('0')
else:        
    while True:
        if m==0: break
        a=m%n
        ans.append(val[a])
        m//=n

    print(''.join(ans[::-1]))