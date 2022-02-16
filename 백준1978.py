def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True

t=int(input())
sum=0
s=list(input().split())
for i in s:
    if isPrime(int(i)): sum+=1
print(sum)