h,m,s=map(int,input().split())
q=int(input())
time=3600*h+60*m+s
for i in range(q):
    method=input()
    if method[0]=='3':
        if time<0:
            while time<0:
                time+=86400
        time%=86400
        H=time//3600
        M=time%3600//60
        S=time%3600%60
        print(H,M,S); continue
    met,how=method.split()
    met=int(met); how=int(how)
    if met==1: time+=how
    if met==2: time-=how