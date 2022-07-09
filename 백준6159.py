N,S=map(int,input().split())
cows=list(int(input()) for _ in range(N))
cows=sorted(cows)
sum=0

left=0; right=1;
while left<=N-1 and right<=N-1:
    if cows[left]+cows[right]<=S:
        sum+=1
    right+=1
    if right==N:
        left+=1; right=left+1;



print(sum)