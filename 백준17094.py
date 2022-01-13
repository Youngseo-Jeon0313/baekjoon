a=int(input())
b=input()
two_sum=0
e_sum=0
for i in range(a):
    if b[i]=='2':
       two_sum+=1
    else :
        e_sum+=1 

if two_sum > e_sum:
    print(2)
elif two_sum < e_sum:
    print('e')
else:
    print('yee')