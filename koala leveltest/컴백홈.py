'''
한수가 집에 돌아가는 경우 중 K가 주어진다면,
그 중 거리가 K인 가짓수를 구하는 것!
'''
road=[]
R, C, K=input().split()

R=int(R)
C=int(C)
K=int(K)

for i in range(R):
    road.append(input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]



print(road)