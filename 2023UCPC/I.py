N, K = map(int, input().split())
energies = list(map(int, input().split()))
rev_energies = energies.copy()
rev_energies = list(reversed(rev_energies))


prefixsum=[]
rev_prefixsum=[]
for i in range(N):
    prefixsum.append(energies[i]+i*K)
    rev_prefixsum.append(rev_energies[i]-i*K)

# print(prefixsum)

min_List=prefixsum.copy()
rev_min_List = rev_prefixsum.copy()
MIN=min_List[-1]
rev_MIN=rev_min_List[0]

for i in range(N-1,-1,-1):
    min_List[i]=MIN
    MIN=min(min_List[i],MIN)

for j in range(N):
    rev_min_List[j]=rev_MIN
    rev_MIN= max(rev_min_List[j], rev_MIN)

for i in range(N):
    prefixsum[i]-=min_List[i]
    rev_prefixsum[i]=rev_min_List[i]
# print(prefixsum)
# print(rev_prefixsum)
prefixsum.pop()
rev_prefixsum[0]=-float('inf')


print(max(max(prefixsum),max(rev_prefixsum)))
