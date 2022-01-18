import sys
arr=[]
for line in sys.stdin:
    arr.append(line.split())

for i in arr:
    n,k=i[0],i[1]
    n=int(n)
    k=int(k)
    answer=n
    while True:
        M=n//k #몫
        N=n%k #나머지
        answer+=M

        n=M+N
        if M<k:
            break
    print(answer)
