"""
N<=8 이라서 브루트포스+dfs 유력
할 수도 있고 안 할 수도 있다 -> 재귀 시 걸었다가 풀었다 가능
"""
def dfs(index):
    global eggs; global N; global answer;
    if index==N:
        broken_eggs = 0
        for j in range(N):
            if eggs[j][0]<=0: 
                broken_eggs+=1
        answer = max(answer, broken_eggs)
        return
    
    if eggs[index][0]<=0:
        dfs(index+1)
        return

    # 자기 말고 다 깨져있는 경우
    Flag = True
    for i in range(N):
        if i==index: continue
        if eggs[i][0]>0:
            Flag=False
            break
    if Flag: answer = max(answer, N-1); return

    for i in range(N):
        if i==index: continue
        if eggs[i][0]<=0: continue
        eggs[i][0]-=eggs[index][1]
        eggs[index][0]-=eggs[i][1]
        dfs(index+1)
        eggs[i][0]+=eggs[index][1]
        eggs[index][0]+=eggs[i][1]

    
answer = 0
N = int(input())
eggs = []
for i in range(N):
    a, b = map(int,input().split())
    eggs.append([a,b])

dfs(0)
print(answer)