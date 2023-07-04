while True:
    a=list(input().split())
    if len(a)==1 and a==['#']: break
    x=a[0]
    ans=0
    for i in range(1, len(a)):
        for j in a[i]:
            if x==j or j.lower()==x: ans+=1
    print(x, ans)