n=int(input())
a,b=0,0 #윗칸, 아래칸
ans=0
while not(a==n and b==n): #이동안 계속 해준다.
    if a>b:
        b+=1
    else:
        a+=1
        b=0
    ans += a+b #계속해서 더하기
print(ans)
