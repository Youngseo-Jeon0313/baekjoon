'''
쉽게 생각해보자.
그렇게 받은 부모노드들을 차곡차곡 저장해서

첫번째 짠 코드

N=int(input())
arr=list(map(int,input().split()))
erase=int(input())
E_list=[]
E_list.append(erase)

for i in range(N):
    if arr[i] in E_list: 
        E_list.append(i)       
Check=[0]*N
for i in range(N):
    if i in E_list : 
        Check[i]=-100
    elif arr[i]>=0: 
        Check[arr[i]]+=1
while len(Check)<N: Check.append(0)
print(Check)
print(E_list)
sum=0
for i in Check: 
    if i==0: sum+=1
print(sum)

내가 짠 이따구 코드에서 자꾸 오류가 나는 이유가 무냐 하면
이게 0-4-3-2-1
     \-5 
이딴식으로 순서에 아예 안 맞게 나오는 경우도 있을 수 있기 때문이다!
'''


'''
재접근

걍 애초에 tree구조부터 망가뜨리는!!!
확인차 for문을 돌면서 tree구조(dictionary)에 넣는데 
없애고자하는 애부터는 아예 무시해버리기
'''
N=int(input())
arr=list(map(int,input().split()))
erase=int(input())
Tree={} #각각의 parent들을 모아놓는 곳

for i in range(N):
    if arr[i]==erase: continue #자 우리가 지우고싶은 노드 등장했다 무시 ㄱ
    elif arr[i] in Tree: Tree[arr[i]].append(i)
    else: Tree[arr[i]]=[i] #없으면 {parent,현재 즉 child} 이렇게 저장

#-1이 없으면 그냥 아무 입력도 안한겨
if -1 not in Tree: print(0); exit()
q=[-1]
ans=0
while q:
    x=q.pop()
    #자식 데려와
    if x in Tree:
        for i in Tree[x]:
            q.append(i)
        if x!=-1 and Tree[x]==[erase]: ans+=1
    else:
        if x !=erase:ans+=1

print(ans)
