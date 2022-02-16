

N=int(input())
i=2#1로 나누어지는 것 제외
while N>1: #자기자신 제외
    if N%i ==0:
        print(i)
        N=N/i
    else: i+=1