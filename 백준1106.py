C,N=map(int,input().split())

List=[]
for _ in range(N):
    cost, clients_num=map(int,input().split())
    List.append([cost, clients_num])

#DP[i]=i명의 고객을 구할 때 필요한 돈의 최솟값
DP=[float('inf') for _ in range(C+100)]  #C는 client라고 생각!
# 100 -> 이 값은 100보다 작거나 같은 자연수이다.

#init
DP[0]=0 

for cost, client_num in List:
    for i in range(C+100):
        if i+client_num<C+100:
            DP[i+client_num]=min(DP[i+client_num], DP[i]+cost)
print(min(DP[C:])) #적어도 C명 늘이기 위해
print(DP)