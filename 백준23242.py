B = int(input())
N = int(input())
List = []
for _ in range(N):
    List.append(int(input()))

dp = [0 for _ in range(N)]
# 자르는 곳의 index 저장
ans = [0, N]

# dictionary로 차이만큼이 어디어디에 있는지 표현하자
diff = [[] for _ in range(100)]
for i in range(N-1):
    diff[abs(List[i+1]-List[i])].append(i+1)
print(diff)
B-=1;
# 일단 가장 크게 점프하는 곳을 자른다.
i = 99
while B and i>=0:
    if diff[i]:
        if len(diff[i])<=B:
            ans+=diff[i]
            B-=len(diff[i])
        #만약 같게 나온다면 이제 여기에서부터는 이분탐색을 해야 한다.
        else:
            break;
    i-=1

#이후 그 다음에 똑같으면 각 등분들 중에서 일정한 값만큼을 자른다.
# 이분탐색
ans=sorted(ans)
print("답", ans)

print("B가 남았는가?",B)
      
if B>0:
    real_ans = []
    # 남아있는 index들은 몇 개로 등분할 것인지에 대한 값
    divide = 0
    # 이분탐색 init
    binary_search = []
    for i in range(len(ans)-1):
        binary_search.append(ans[i+1]-ans[i])
    start = 0; end = N
    while start <= end:
        mid = (start+end)//2
        temp = 0
        for i in binary_search:
            temp+=i//mid-1
        if temp >= B: # 범위를 더 늘려야 함
            start = mid
        else:
            divide = mid
            end = mid-1
    print('경계', divide)
    for i in range(len(ans)):
        real_ans.append(ans[i])
        if i<len(ans)-1:
            add = ans[i]+divide
            while B>0 and add<ans[i+1]:
                real_ans.append(add);
                B-=1
                add+=divide
else:
    real_ans = ans
print(real_ans)

prefix_sum = [0 for _ in range(N+1)]
for i in range(1,N+1):
    prefix_sum[i]=prefix_sum[i-1]+List[i-1]

ret = 0

print(prefix_sum)
for i in range(1,len(real_ans)):
    mean = (prefix_sum[real_ans[i]]-prefix_sum[real_ans[i-1]])/(real_ans[i]-real_ans[i-1])
    for j in range(real_ans[i-1],real_ans[i]):
        ret+=(List[j]-mean)**2

print('{0:.6f}'.format(ret))
