'''
from itertools import combinations
import math
t=int(input())
for i in range(t):
    MIN=1.5*10**5
    S=[]
    num=int(input())
    arr=list(list(map(int,input().split())) for _ in range(num))
    if num>=4:
        num=list(i for i in range(num))
        for i,j,k,l in list(combinations(num,4)):
            S.append([i,j,k,l])
    else: 
        S=list(list(i for i in range(num)))
    if len(S)==2: 
        for a,b in list(combinations(S,2)):
            v=math.sqrt((arr[a][0]-arr[b][0])**2+(arr[a][1]-arr[b][1])**2)
        print(v)
        exit();
    else:
        for s in S:
            a=min(math.sqrt((arr[s[0]][0]-arr[s[1]][0]+arr[s[2]][0]-arr[s[3]][0])**2+(arr[s[0]][1]-arr[s[1]][1]+arr[s[2]][1]-arr[s[3]][1])**2),math.sqrt((arr[s[0]][0]-arr[s[1]][0]-(arr[s[2]][0]-arr[s[3]][0]))**2+(arr[s[0]][1]-arr[s[1]][1]-(arr[s[2]][1]-arr[s[3]][1]))**2))
            b=min(math.sqrt((arr[s[0]][0]-arr[s[2]][0]+arr[s[1]][0]-arr[s[3]][0])**2+(arr[s[0]][1]-arr[s[2]][1]+arr[s[1]][1]-arr[s[3]][1])**2),math.sqrt((arr[s[0]][0]-arr[s[2]][0]-(arr[s[1]][0]-arr[s[3]][0]))**2+(arr[s[0]][1]-arr[s[2]][1]-(arr[s[1]][1]-arr[s[3]][1]))**2))
            c=min(math.sqrt((arr[s[0]][0]-arr[s[3]][0]+arr[s[1]][0]-arr[s[2]][0])**2+(arr[s[0]][1]-arr[s[3]][1]+arr[s[1]][1]-arr[s[2]][1])**2),math.sqrt((arr[s[0]][0]-arr[s[3]][0]-(arr[s[1]][0]-arr[s[2]][0]))**2+(arr[s[0]][1]-arr[s[3]][1]-(arr[s[1]][1]-arr[s[2]][1]))**2))
            if min(a,b,c)<MIN: MIN=min(a,b,c)
    print(MIN)

문제 이해가 어려움...ㅠㅠ
벡터 두 개를 뽑자는 문제가 아니다!!
모든 점을 한 번씩 써서 n/2개의 벡터를 만들고
그의 합인 벡터의 길이가 최소가 되도록해야 함
'''
from itertools import combinations
import math
t=int(input())
for i in range(t):
    MIN=float('inf')
    arr=[]
    num=int(input())
    total_x=0; total_y=0;
    for i in range(num):
        x,y=map(int,input().split())
        arr.append([x,y])
        total_x+=x
        total_y+=y
    S=list(combinations(arr,num//2))
    Slen=len(S)//2
    print(S)
    for i in S:
        T_x=total_x; T_y=total_y;
        for j in i:
            T_x-=2*j[0]
            T_y-=2*j[1]
        if math.sqrt(T_x**2+T_y**2)<MIN: MIN=math.sqrt(T_x**2+T_y**2)
    print(MIN)


