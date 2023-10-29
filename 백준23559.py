'''
일단 1000원으로 다 먹인다 
이후 5000원으로 대체할 수 있는 날들을 선택해서 바꾼다. 이 때 이게 무슨 날인지는 몰라도 됨
그러면 정렬조건은 5000원 짜리와 1000원 짜리의 차이가 된다.
'''

N, X = map(int,input().split())
menu = []

ans = 0
for _ in range(N):
    a,b=map(int,input().split())
    menu.append([a,b])
#일단 1000원으로 다 먹인다.
for i in range(N):
    X-=1000
    ans+=menu[i][1]

#정렬한다.
menu = sorted(menu, key = lambda x:[x[1]-x[0]])
print(menu)
for i in menu:
    if i[1]<i[0] and X-4000>=0:
        ans=ans-i[1]+i[0]
        X-=4000
        print('ans',ans)

print(ans)