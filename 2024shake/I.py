#오큰수 범위의 최댓값
N = int(input())
List = list(map(int,input().split()))

max_value = [0 for _ in range(N)]
stack = []
for i in range(N-1, -1, -1): #뒤에서부터 측정한다.
    while stack and stack[-1][1]<List[i]:
        a = stack.pop()
    if stack:
        max_value[i]=stack[-1][0]-i
    stack.append([i, List[i]]) #내 인덱스랑 값

#print(max_value)
ans = 0
for index in range(N):
    if max_value[index]==0:
        ans = max(ans, N-index)
    else:
        ans = max(ans, max_value[index])

print(ans)
'''
13
2 4 3 6 10 1 8 5 12 3 17 72 36
'''