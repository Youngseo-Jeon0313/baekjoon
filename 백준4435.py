T=input()
T=int(T)

for i in range(T):
    small_sum=0
    big_sum=0
    a,b,c,d,e,f=map(int, input().split())
    A,B,C,D,E,F,G=map(int, input().split())

    small_sum+=a*1
    small_sum+=b*2
    small_sum+=c*3
    small_sum+=d*3
    small_sum+=e*4
    small_sum+=f*10
    big_sum+=A*1
    big_sum+=B*2
    big_sum+=C*2
    big_sum+=D*2
    big_sum+=E*3
    big_sum+=F*5
    big_sum+=G*10
    print("Battle ",i+1,':', sep='',end=' ')
    if small_sum>big_sum:
        print("Good triumphs over Evil")
    elif small_sum < big_sum:
        print("Evil eradicates all trace of Good")
    else:
        print("No victor on this battle field")
