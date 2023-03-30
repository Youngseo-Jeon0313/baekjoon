T=int(input())
for _ in range(T):
    N=int(input())
    K=int(input())
    List=[a+1 for a in range(K)]
    for i in range(N):
        for k in range(1,K):
            List[k]=List[k]+List[k-1]
    # print(List)
    print(List[-1])
'''
1 3 -> 1,2,3
2 3 -> 1 3(1+2), 6(1+2+3)
'''
