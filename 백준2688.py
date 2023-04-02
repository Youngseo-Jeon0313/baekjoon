T=int(input())
for _ in range(T):
    n=int(input())
    prefix_sum=[i+1 for i in range(10)]
    for turn in range(n-1):
        for j in range(1,10):
            prefix_sum[j]+=prefix_sum[j-1]
    # print(prefix_sum)
    print(prefix_sum[-1])