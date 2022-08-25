arr=[
[1, 2, 3, 4, 5],
[11,12,13,14,15],
[21,22,23,24,25],
[31,32,33,34,35],
[41,42,43,44,45],
]

N=5

for i in range(N): #차이
    for j in range(N-i):
        print(arr[j][i+j],end=' ')
    print()