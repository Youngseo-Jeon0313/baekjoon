#00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수 출력

h=int(input())

count = 0
for i in range(h+1): #여기서 i는 한 시간씩 늘어나는 걸로 그럴 때마다 60까지만 계속 새주면 됨!
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)