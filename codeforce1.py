n=int(input())
for _ in range(n):
    num=int(input())
    if num>=1900: print("Division",1)
    elif num>=1600: print("Division",2)
    elif num>=1400: print("Division",3)
    else: print("Division",4)

    