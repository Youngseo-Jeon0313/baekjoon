BIGNUM = 100
visited = [True for _ in range(10**9)]

for num1 in range(1,BIGNUM): #일단 하나씩 돌아가면서 다른 애들과 판단할 예정이다.
    if not visited[num1]: continue # 여기 이미 안된다고 체크됐으면 얘는 빼야 됨
    for num2 in range(1, num1):
        if (num1*num2)%(num1+num2)==0:
            print(num1, num2, (num1*num2)//(num1+num2))
            visited[num1]=False
            visited[num1*num2]=False

import sys
input=sys.stdin.readline
n=int(input())
ans = []
for i in range(10**9):
    if visited[i]: continue
    else: ans.append(i)
print(ans[:10])