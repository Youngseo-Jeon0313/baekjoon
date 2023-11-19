N, K = map(int,input().split())
List = list(map(int,input().split()))
K-=1
'''
(Ka-K0) + (Kb-Ka+1) + (Kc-Kb+1)
= (Kc-K0) + (Kb-Kb+1) + (Ka-Ka+1)
'''
max_index = []
for i in range(N-1):
    max_index.append([i, List[i]-List[i+1]])
answer = List[-1]-List[0]
max_index = sorted(max_index, key=lambda x:x[1])
k=0
for j in max_index:
    index = j[0]
    if k==K: break;
    answer += List[index]-List[index+1]
    k+=1

print(answer)