import copy

N, K = map(int,input().split())
result = list(map(int,input().split()))
pattern = list(map(int,input().split()))
for i in range(N):
    result[i]-=1
    pattern[i]-=1

# 정답으로 가기 위한
ans = copy.deepcopy(result)
for i in range(K): # 몇 번 이 짓을 ?
    temp = copy.deepcopy(ans)
    for j in range(N):
        # 이 중간중간 단계를 메모해둘 temp
        a = pattern[j]
        temp[a] = ans[j]
    ans = copy.deepcopy(temp)

for i in range(N):
    ans[i] +=1
print(*ans)


