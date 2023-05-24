a=list(map(int,input().split()))
flag=True
for i in a:
    if i not in (0,1):
        flag=False;
if flag: print("S")
else:    print("F"); 