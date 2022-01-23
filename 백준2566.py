arr = []
for i in range(9):
    arr.append(list(map(int,input().split())))

max=0
for i in range(9):
    for j in range(9):
        if arr[i][j]>max:
            max=arr[i][j]

for i in range(9):
    for j in range(9):
        if arr[i][j]==max:
            print(max)
            print (i+1,j+1)