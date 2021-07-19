list=[]
for i in range(9):
    list.append(int(input()))

max=list[0]
max_order=0
for i in range(9):
    if list[i]>=max:
        max_order=i
        max=list[i]

print(max,max_order+1,sep='\n')