import sys
input=sys.stdin.readline

N,a,b=map(int,input().split())

for i in range(b,-1,-1):
    div=1
    index=0
    temp=i
    while temp>1:
        div*=2
        index+=1
        if temp//div==1:
            if a//div==0: print(index+1); exit()
            else:
                print(index);exit()
    