T=int(input())

for i in range(T):
    S=input()
    sum=0
    for i in range(65,65+26):
        if chr(i) not in S:
            sum+=i
    print(sum)