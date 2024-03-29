N, K = map(int, input().split())
energies = list(map(int, input().split()))

prefixsumN=[]
prefixsumS=[]

for i in range(N):
    prefixsumN.append(energies[i]+i*K)
    prefixsumS.append(energies[i]-i*K)

# print(prefixsum)

N_List=prefixsumN.copy()
S_List=prefixsumS.copy()
N_MIN=N_List[-1]
S_MIN=S_List[0]
for i in range(N-1,-1,-1):
    N_List[i]=N_MIN
    N_MIN=min(N_List[i],N_MIN)

for i in range(N):
    S_List[i]=S_MIN
    S_MIN=min(S_List[i],S_MIN)

for i in range(N):
    prefixsumN[i]-=N_List[i]
    prefixsumS[i]-=S_List[i]


prefixsumN[-1]=-float('inf')
prefixsumS[0]=-float('inf')

# print(prefixsumN)
# print(prefixsumS)
print(max(max(prefixsumN), max(prefixsumS)))
