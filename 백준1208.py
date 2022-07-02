from itertools import combinations as cb
#기존 투포인터 방식과 다른 점은
# 우리가 받은 arr를 두 개로 쪼개서 해결하면 시간복잡도가 더 줄어든다는 것이다.

N,S=map(int,input().split())
arr=list(map(int,input().split()))
arr1=arr[:N//2]
arr2=arr[N//2:] #포함이 안되니까 이리도 간단한 것을~
SumList1=[]
SumList2=[]

for i in range(len(arr1)+1):
    for j in cb(arr1,i):
        SumList1.append(sum(j))

for i in range(len(arr2)+1):
    for j in cb(arr2,i):
        SumList2.append(sum(j))

SumList1=sorted(SumList1)
SumList2=sorted(SumList2)
answer=0
left_pointer=0; right_pointer=len(SumList2)-1
while right_pointer>=0 and left_pointer<len(SumList1):
    if SumList1[left_pointer]+SumList2[right_pointer]==S:
        #겹치는 경우도 생각해보자. [2,2,3] [1,4,4] 이렇게 !
        left_rap=1; right_rap=1
        #while 문으로 해결
        while left_pointer+1<len(SumList1) and SumList1[left_pointer+1]==SumList1[left_pointer] : #이렇게 해야 그 바로 오른쪽이 다르면 애초에 들어가지도 않음
            left_pointer+=1; left_rap+=1
        while right_pointer-1>=0 and SumList2[right_pointer-1]==SumList2[right_pointer] :
            right_pointer-=1; right_rap+=1
        answer+=left_rap*right_rap
        right_pointer-=1; left_pointer+=1;
    elif SumList1[left_pointer]+SumList2[right_pointer] > S:
        right_pointer-=1
    else: left_pointer+=1
if S==0:
    print(answer-1)
else: print(answer)