W=[]; K=[];
for _ in range(10):
    W+=[int(input())]
for _ in range(10):
    K+=[int(input())]

W=sorted(W)
K=sorted(K)

w=0; k=0
w+=W[-1]+W[-2]+W[-3]
k+=K[-1]+K[-2]+K[-3]

print(w, k)
