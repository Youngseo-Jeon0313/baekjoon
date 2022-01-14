N, step=map(int,input().split())
List=list(map(int, input().split(',')))

for i in range(step):
    for i in range(N-1):
        List[i]=(List[i+1]-List[i])

for i in range(N-step-1):
    print(List[i], end=',')
print(List[N-step-1])