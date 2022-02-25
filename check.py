import math
def jegob(n):
    if int(math.sqrt(n))**2==n: return True
    return False

print(jegob(95481))