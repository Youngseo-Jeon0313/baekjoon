num_List=list()
odd=list()
for i in range(7):
    num_List.append(int(input()))

for i in num_List:
    if i%2!=0:
        odd.append(i)


if len(odd)==0:
    print(-1)
else:
    sum=0
    for i in odd:
        sum+=i
    print(sum)
    print(min(odd))