check=['5','8']

T=int(input())
for _ in range(T):
    totallist=[]
    N1=int(input())
    numlist1=list(map(int,input().split()))
    N2=int(input())
    numlist2=list(map(int,input().split()))
    N3=int(input())
    numlist3=list(map(int,input().split()))
    sum=0
    for i in numlist1:
        for j in numlist2:
            for k in numlist3:
                a=i+j+k
                a=str(a)
                flag=True
                for x in a:
                    if x not in check:
                        flag=False
                if flag==True and a not in totallist: sum+=1; totallist.append(a)
    print(sum)
    
    
