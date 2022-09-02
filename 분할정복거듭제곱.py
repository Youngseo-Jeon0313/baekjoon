def fpow(c,n):
    if n==1: return c
    else: 
        x=fpow(c,n//2)
        if n%2:return x*x*c
        else: return x*x
        