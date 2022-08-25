T=int(input())
for _ in range(T):
    sum=0; flag=True
    x=input()
    y=x[::-1]
    for i in range(len(x)//2+1):
        if x[i]==y[i]: sum+=1
        else: flag=False; sum+=1; break
    print(int(flag), (sum))