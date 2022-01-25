n=int(input())
s=input()
sum_A=0
sum_B=0
for i in s:
    if i=='A':
        sum_A+=1
    else:
        sum_B+=1
if sum_A>sum_B:
    print('A')
elif sum_B>sum_A:
    print('B')
else:
    print('Tie')