t = int(input())
for i in range(t):
    a, b = input().split()

    ans=[]
    for j in range(len(a)):
        x=ord(a[j])-64
        y=ord(b[j])-64
        if y>=x: z= y-x
        else: z=y +26 -x #절대값으로 해도 될 것 같은디
        ans.append(z)
    print('Distances: {}'.format(' '.join(map(str, ans))))