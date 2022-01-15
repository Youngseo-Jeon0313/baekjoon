T=int(input())

for i in range(T):
    arr=tuple(map(int, input().split()))
    HP=arr[0] +arr[4]
    if HP<1: HP=1
    MP =arr[1] +arr[5]
    if MP < 1: MP =1
    ATK = arr[2] + arr[6]
    if ATK <0 : ATK = 0
    DEF = arr[3] + arr[7]
    print(HP + 5*MP + 2*ATK + 2*DEF)