import math
A,B=input().split()
Len=max(len(A),len(B))
A=A.rjust(Len,'0')
B=B.rjust(Len,'0')
ans=[]
print(A,B)
for i in range(Len):
    ans+=[str(int(A[i])+int(B[i]))]

print(''.join(ans))