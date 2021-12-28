n=int(input())
data=list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data:
    count +=1 #count를 1씩 올리면서 계속 파악
    if count >= i:
        result += 1 #전체적인 갯수를 의미하는 result 더하고
        count = 0 #다시 count는 0으로 초기화

print(result)