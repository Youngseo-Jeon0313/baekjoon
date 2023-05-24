for _ in range(3):
    a,b,c,d,e,f=map(int,input().split())
    ans=60*60*d+60*e+f-(60*60*a+60*b+c)
    print(ans//3600, ans%3600//60, ans%60%60)