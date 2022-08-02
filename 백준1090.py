'''
완전탐색 
'''

N=int(input())
ans=[float('inf') for _ in range(N)]
ans[0]=0
List=[]
for i in range(N):
    x,y=map(int,input().split())
    List.append([x,y])
for i in range(N): #해당 점이 x의 중심 그리고 또 어떤 해당 점이 y의 중심이라고 가정한다.(맨허튼)
    for j in range(N):
        list=[]
        for k in range(N): #다른 점들을 둘러본다.
            list.append(abs(List[k][0]-List[i][0])+abs(List[k][1]-List[j][1]))
        list=sorted(list)
        sum=0
        for k in range(N): #거리만큼을 더한다. (N경우까지 갱신)
            sum+=list[k]; 
            if ans[k]>sum: ans[k]=sum
print(*ans)




