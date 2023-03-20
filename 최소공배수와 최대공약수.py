def lcm(a, b):
    for i in range(max(a, b), (a * b) + 1):
        if i % a == 0 and i % b == 0:
            return i
        
#또는
def gcd(a, b):  # 최대공약수
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b / gcd(a, b)