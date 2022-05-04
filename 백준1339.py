#0 1 2 3 4 5 6 7 8 9 
N=int(input()) #1이상 10이하
L=list()
for _ in range(N): L.append(input())
for i in range(N):
    for j in range(i):
        