import sys
input=sys.stdin.readline

X=int(input())
numarr=[0 for _ in range(10)]
for i in str(X):
    numarr[int(i)]+=1
for j in range(X+1,999999):
    arr=[0 for _ in range(10)]
    for k in str(j):
        arr[int(k)]+=1
    if arr==numarr: print(j); exit();
print(0)