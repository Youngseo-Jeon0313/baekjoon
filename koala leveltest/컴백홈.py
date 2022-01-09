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
    road.append((input().split()))

print(road)
making_road=[[0 for col in range(C)] for row in range(R)]
print(making_road)

for i in range(R):
    for j in range(C):
        if (road[i])[j]=='T':
            making_road[i][j]=0
        elif j==0 or i==R-1:
            making_road[i][j]=1
        else:
            making_road[i][j]=0


for i in range(1,R-1):
    for j in range(1,C):
        if road[i][j]=='T':
            making_road[i][j]=0
        else:
            if road[i+1][j]=='T':
                making_road[i][j]+=making_road[i][j-1]
            elif road[i][j-1]=='T':
                making_road[i][j]+=making_road[i+1][j]
            else:
                making_road=making_road[i][j-1]+making_road[i+1][j]

print(making_road)