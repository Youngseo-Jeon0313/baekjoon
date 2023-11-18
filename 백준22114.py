N, K = map(int, input().split())
List = list(map(int,input().split()))

check = [0 for _ in range(N)]
answer = 0

# 가능한 것들을 먼저 찾아보자
for i in range(N-1):
    if List[i]<=K: check[i]=1

front = [0 for _ in range(N)]
back = [0 for _ in range(N+1)]

for i in range(N-1):
    if check[i]:
        front[i+1]=front[i]+1

for j in range(N-2,-1,-1):
    if check[j]:
        back[j+1]=back[j+2]+1

# print(front)
# print(back)
answer = 0
flag=False


if N==2:
    answer = 2

elif N==3:
    num = 0
    for i in List:
        if i<=K: num+=2
    answer = max(2, num+1)
else:
    for k in range(N-2):
        if front[k]==0 and back[k+2]==0: 
            answer = max(answer, 2)
        elif front[k]==0:
            answer = max(answer, back[k+2]+2)
        elif back[k+2]==0: 
            answer = max(answer, front[k]+2)
        else: 
            answer = max(answer, front[k]+back[k+2]+2)


print(answer)
'''
test case

7 3
4 4 4 4 4 3
3

7 3
4 4 4 4 4 4
2

2 1
1
2

3 2
1 4
3

'''


'''
만약 최대 두 번이라면??
'''