N=int(input())
List=list(map(int,input().split()))
Max=0
for i in range(N):
    localmax=0
    start1=i; slope1=-float('inf')
    start2=i; slope2=-float('inf')
    while True: #왼쪽으로 가면서 개수 출력
        start1-=1
        if start1<=-1: break
        if (List[i]-List[start1])/(start1-i)>(slope1):slope1=(List[i]-List[start1])/(start1-i);localmax+=1
    while True: #오른쪽으로 가면서 개수 출력
        start2+=1
        if start2>=N: break
        if (List[start2]-List[i])/(start2-i)>(slope2): slope2=(List[start2]-List[i])/(start2-i); localmax+=1
    Max=max(Max,localmax)
    
print(Max)