import sys
input=sys.stdin.readline

n=1000001
arr = [True]*(n+1)


for i in range(2,n+1):
  if arr[i]:
    for j in range(2*i, n+1, i):
        arr[j] = False

while True:
    num=int(input())
    if num==0: break
    flag=False;
    for i in range(3,len(arr)):
        if arr[i] and arr[num-i]:
            flag=True
            print(num,'=',i,'+',num-i); break;
    if flag==False: print("Goldbach's conjecture is wrong.");
    