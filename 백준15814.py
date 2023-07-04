S=list(input())
T=int(input())
for _ in range(T):
    a,b=map(int,input().split())
    S[a],S[b]=S[b],S[a]
print(''.join(S))