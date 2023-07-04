T=int(input())
for _ in range(T):
    a=int(input())
    b=a*a
    Len=len(str(a))
    if str(b)[-Len:]==str(a):
        print("YES")
    else: print("NO")



