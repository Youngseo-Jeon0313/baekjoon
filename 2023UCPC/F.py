import sys

N, Q = map(int, sys.stdin.readline().split())

people = [[0]*N for _ in range(N)]
count = 1

for i in range(N):
    for j in range(N):
        people[i][j] = (i)*N + j+1

for _ in range(Q):
    temp = sys.stdin.readline().strip()
    if temp == "RO":
        for i in range(N):
            if i%2 == 0:
                record = people[i][N-1]
                for j in range(N -1, 0, -1):
                    people[i][j] = people[i][j-1]
                people[i][0] = record
    elif temp == "RE":
        for i in range(N):
            if i%2 == 1:
                record = people[i][N-1]
                for j in range(N -1, 0, -1):
                    people[i][j] = people[i][j-1]
                people[i][0] = record
    elif temp == "CO":
        for i in range(N):
            if i%2 == 0:
                record = people[N-1][i]
                for j in range(N -1, 0, -1):
                    people[j][i] = people[j-1][i]
                people[0][i] = record
    elif temp == "CE":
        for i in range(N):
            if i%2 == 1:
                record = people[N-1][i]
                for j in range(N -1, 0, -1):
                    people[j][i] = people[j-1][i]
                people[0][i] = record
    elif temp[0] == "S":
        dot = temp.split()
        people[int(dot[1]) - 1][int(dot[2]) - 1], people[int(dot[3]) - 1][int(dot[4]) - 1] = people[int(dot[3]) - 1][int(dot[4]) - 1], people[int(dot[1]) - 1][int(dot[2]) - 1]
    else:
        print("error")

for i in range(N):
    print(*people[i])