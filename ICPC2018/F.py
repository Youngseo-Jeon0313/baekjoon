import sys
input=sys.stdin.readline

W,N=map(int,input().split())
L=list(map(int,input().split()))
check=[0 for _ in range(W+1)]

#5 10 7 3 2 1

for i in range(N): #구간을 쪼개는
    for j in range(i+1,N):
        if L[i]+L[j]>W or L[i]+L[j]<0:continue
        if check[(W-L[i]-L[j])]: print('YES'); exit()
    for j in range(i):
        if L[i]+L[j]>W or L[i]+L[j]<0: continue
        check[L[i]+L[j]]=1;

print('NO')