max=0; max_index=0
for i in range(5):
    a,b,c,d=map(int,input().split())
    if a+b+c+d>max: max=a+b+c+d; max_index=i+1

print(max_index, max)