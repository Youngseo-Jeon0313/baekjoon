import math
#for문 + 조회
N,Q=map(int,input().split())
List=list(map(int,input().split()))
arr=[0 for _ in range(10001)]
for i in range(N):
    arr[List[i]]+=1

for _ in range(Q):
    a,b=map(int,input().split())
    flag=True
    if a==1:
        # ZeroDivision
        if b==0 and arr[0]>0: print(1); flag=False;
        else:
            for i in range(1,10001):
                if b%i==0 :
                    #제곱일 경우
                    if i*i==b:
                        if arr[i]>=2:
                            print(1); flag=False; break
                    else:
                        if arr[i]>0 and len(arr)>b//i and arr[b//i]>0: 
                            print(1); flag=False; break
        if flag: print(0)
    elif a==2 :
        arr[List[b-1]]-=1; arr[0]+=1; List[b-1]=0