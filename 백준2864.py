A,B=input().split()
A_min=list(A).copy()
A_max=list(A).copy()
for i in range(len(A)-1,-1,-1):
    if A[i]=='5': A_max[i]='6'
    elif A[i]=='6': A_min[i]='5'
B=list(B)
B_min=list(B).copy()
B_max=list(B).copy()
for j in range(len(B)-1,-1,-1):
    if B[j]=='5': B_max[j]='6'
    elif B[j]=='6': B_min[j]='5'

print(int(str(''.join(A_min)))+int(str(''.join(B_min))))
print(int(str(''.join(A_max)))+int(str(''.join(B_max))))