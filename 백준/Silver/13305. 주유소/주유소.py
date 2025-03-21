N = int(input())
roads = list(map(int,input().split()))
new_road_list = []
gas_stations = list(map(int,input().split()))
answer = 0
MIN = float('inf')
for i in range(N):
    if gas_stations[i]<MIN:
        new_road_list.append(gas_stations[i])
        MIN = gas_stations[i]
    else:
        new_road_list.append(MIN)
# print(new_road_list)
for i in range(N-1):
    answer += roads[i]*new_road_list[i]
print(answer)