'''
최소 몇 번 점프를 해야 갈 수 있는지??
최단경로 문제.
배열을 하나 만든 다음에,
거기까지 갈 수 있는 최단 경로를 계속 업데이트 시키자!

'''
a=int(input())
jump=list(map(int, input().split()))

least=[0 for i in range(a)]


for i in range(1,a):
    type=[]
    for j in range(i):
        if (i-j) <= jump[j]:
            type.append(least[j]+1)
        else:
            type.append(100000)
    if min(type)==100000:
        least[i]=0
        break
    else:
        least[i]=min(type)

if least[-1]==0:
    if a ==1:
        print(0)
    else:
        print(-1)
else:
    print(least[a-1])