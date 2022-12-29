t=int(input())

#백만큼 더하라
num_list=[i for i in range(100)]
for i in range(1,100): num_list[i]=num_list[i-1]+num_list[i]

print(num_list)

for _ in range(t):
    m,s=map(int,input().split())
    L=list(map(int,input().split()))
    Max=max(L)
    flag=False
    for i in range(100):
        if s+sum(L)==num_list[i] and Max<=i: flag=True
    if flag: print("YES")
    else: print("NO")