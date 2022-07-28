import sys
input=sys.stdin.readline

N,K=map(int,input().split())
monsters=list(map(int,input().split()))
PEOPLE=list(map(int,input().split()))
ans=0
#dfs는 parameter를 뭘로 설정할지가 가장 중요하다
'''
-방문한 마을 리스트
-남아있는 체력값
-지금까지 구한 주민 수
이건 O(20!) = 3628800 XXXXX!!!!!!!!
만약에 조합으로 할 경우에는 O(2^20) =1048576
'''
def dfs(visited,health,people):
    #처리한다
    global ans
    
    for i in range(N):
        if i in visited:continue
        else:
    #dfs간다   
            if visited:
                sum=0
                for j in visited:
                    sum+=monsters[j]
                if health-sum-monsters[i]>=0:
                    dfs(visited+[i], health-sum-monsters[i], people+PEOPLE[i])
            else:
                if health-monsters[i]>=0:
                    dfs(visited+[i], health-monsters[i],people+PEOPLE[i])
    ans=max(ans,people)
    # print('짠:',visited,health,people)
    #다시원위치로
dfs([],K,0)
print(ans)