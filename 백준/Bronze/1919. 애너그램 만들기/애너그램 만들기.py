ans=0
a=input()
b=input()
A=[0 for _ in range(27)]
B=[0 for _ in range(27)]

for i in range(len(a)):
    A[ord(a[i])-97]+=1
for k in range(len(b)):
    B[ord(b[k])-97]+=1

for j in range(27):
    ans+=abs(A[j]-B[j])
print(ans)