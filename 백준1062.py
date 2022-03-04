from itertools import combinations as cb


Alphalist=[2,4,5,6,7,8,10,11,12,13,15,16,17,18,19,21,22,23,24,25,26]
#-96
#1,3,9,14,20
N,K=map(int,input().split())
if K<5: print(0); exit()
elif K==5: #a,c,i,n,t
    ALPHA=[1,3,9,14,20]
    arr=[]
    for i in range(N):
        arr.append(input())
    sum=0
    for i in arr:
        flag=True
        for j in i: 
            if (ord(j)-96) not in ALPHA: flag=False; break
        if flag==True: sum+=1
    print(sum)
else: 
    SUM=[]
    ALPHA=[1,3,9,14,20]
    arr=[]
    for i in range(N):
        arr.append(input())
    for x in cb(Alphalist,K-5):
        sum=0
        ALPHA=[1,3,9,14,20]
        ALPHA.extend(x)
        for i in arr:
            flag=True
            for j in i: 
                if (ord(j)-96) not in ALPHA: flag=False; break
            if flag==True: sum+=1
        SUM.append(sum)

    print(max(SUM))    
    