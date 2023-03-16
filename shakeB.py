import sys
input=sys.stdin.readline

N=int(input())
primes=map(int,input().split())
K=int(input())

def top(n,m,index):
    compare=1
    while True:
        compare*=m
        if compare>n: break
        index+=1
    return index

ans=0
for i in primes:
    #가장 상위에 있는 지수부터 내려오기
    before=0
    top_root=top(K,i,0)
    # print(top_root)
    for j in range(top_root,0,-1):
        divided=i**j
        # print(divided,i,j)
        ans+=(K//divided-before)*j
        before=K//divided
print(ans)