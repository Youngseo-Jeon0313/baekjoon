a=int(input())

for i in range(1,a+1):
    list_i=list(str(i))
    for j in range(len(list_i)-1):
        list.append(list_i[j]-list_i[j+1])

for i in range(len(list)):
    for j in range(len(list)):
        if i!=j:
            break
        else:
            continue