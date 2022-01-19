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
        answer+=M #answer에 더하는 값
        n=M+N #확인용
        if n<k :
            break
    print(answer)