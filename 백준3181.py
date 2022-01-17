NO={'i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili'}

L=list(input().split())
for i in NO:
    th=0
    for j in L:
        if j==i and th!=0:
            L.pop(th)
        th+=1
for i in L:
    print(i[0].upper(),end='')