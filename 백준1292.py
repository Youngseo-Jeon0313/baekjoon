L=list()


for i in range(50):
    for j in range(i):
        L.append(i)

start,end=map(int, input().split())

sum=0
for i in range(start, end+1):
    sum+=L[i-1]

print(sum)