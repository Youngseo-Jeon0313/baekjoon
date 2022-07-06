def issquare(a,b):
    n=a*b
    sqrt = n ** (1/2)
    if sqrt % 1 ==0: return True
    else: return False

print(issquare(10**3, 139282434))