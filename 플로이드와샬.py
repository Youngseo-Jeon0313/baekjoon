'''
다익스트라인데 모든 정점 -> 모든 정점
A정점 -> A정점 갈 수 있으면 0 / 못 가면 무한대로 초기화

DP 느낌
shortestPath(i, j, k)라는 문제는 i번 정점에서 j번 정점까지, 1~k번 정점만 사용할 때의 최단 거리를 구하라는 의미입니다.
이번에는 k 정점도 반영하면 i,j까지의 거리는 뭐가 최소냐.
이런 느낌으로 k=1~n-1까지 돌 때 i,j도 1~N 1~N까지 돈다.

'''
#입력
n = int(input())
m = int(input())
bus_cost = [[100001 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    bus_cost[start][end] = min(cost, bus_cost[start][end])

#플로이드-워셜 알고리즘
for k in range(1, n+1): #경로 for문이 가장 상위 단계여야 누락되지 않는다
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j: #자기 자신으로 오는 경우는 없다고 했으므로
                bus_cost[i][j] = 0 
            else: #경로 거치는 것 or 직접 가는 것 or 이전 경로들
                bus_cost[i][j] = min(bus_cost[i][j],
                                     bus_cost[i][k] + bus_cost[k][j])


#출력
for row in bus_cost[1:]:
    for col in row[1:]:
        if col == 100001:
            print(0, end = " ")
        else:
            print(col, end = " ")
    print()