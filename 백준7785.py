company = dict()
n = int(input())
for i in range(n):
    x, y = input().split()
    company[x] =y
#입력받을 때 이미 만약 leave인 사람이 있으면 갱신이 되어버림
key=list(company.keys())
ans=[]
for i in range(len(key)):
    if company[key[i]]=='enter':    #value 값이 enter이 있다면
        ans.append(key[i])

ans.sort(reverse=True)  #사전 순의 역순으로 출력
for i in range(len(ans)): 
    print(ans[i])
