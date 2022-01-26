def factorial(x):
    global ans
    ans *= x
    if x != n: 
        return factorial(x+1)
    

n = int(input())
if n==0:
    print(1)
    exit()
ans = 1
factorial(1)

print(ans)