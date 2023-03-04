import sys
input=sys.stdin.readline

#최대한 많은 줄에 탭을 추가하거나 삭제해야 하므로
#첫째줄부터 끝까지 탐색해가며 묶음으로 처리한다.
#그리디

N=int(input())
before=list(map(int,input().split()))
after=list(map(int,input().split()))

count=0
condition = [0,1,2]
check=0

while after != before:
    for i in range(N):
        if before[i]==after[i]:
            check=0 
        elif before[i]>after[i]:
            if check!=1:
                count+=1
                before[i]-=1
                check=1
            else:
                before[i]-=1
        else:
            if check!=2:
                count+=1
                before[i]+=1
                check=2
            else:
                before[i]+=1
    check=0
print(count)