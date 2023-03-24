lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27]
i = 28
while len(lst) < 1000000:
    number = [0]*10
    k = str(i)
    for j in k:
        j = int(j)
        if number[j]:
            break
        else:
            number[j] = 1
    else:
        lst.append(k)
    i += 1

while True:
    n = int(input())
    if n == 0:
        break
    print(lst[n-1])