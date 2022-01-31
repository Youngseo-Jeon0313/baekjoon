'''
허무하다..
이거는 사실상 나중에 set해주나 
아예 처음부터 set해주나 상관ㅇㅣ 없음 ㅠㅠ


그리고 조금 생각해줘야 되는 게 
''.join(map(str, arr)) 
이렇게 해줄 때는 이게 무조건 str으로 되는 거 조심 ㅠㅠ
근데 또 7 9 이렇게 저장했으면 이걸 또 어떻게 sort 조질거냐고ㅠㅠ

'''
N,M=map(int,input().split())
L=list(map(int,input().split()))

def solve(num,ans):
    if len(ans)==num :
        for i in ans:
            print(L[i],end=' ')
        print()
        return
    for i in range(0,len(L)):
        solve(num,ans+[i]) #새로운 애로 바꿔주기
L=list(set(L))
L.sort()
for i in range(len(L)):
    solve(M,[i])