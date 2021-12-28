#chess를 둘 때 옆으로 2칸 밑으로 한 칸 또는 옆으로 한 킨 밑으로 두 칸 이런 식으로만 갈 수 있다고 치자!
#이동할 수 있는 위치는 총 몇 군데인지??

#현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0]))-int(ord('a'))+1

#나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1,-2), (2,-1), (2,1),(1,2),(-1,2),(-2,1)]

#8가지 방향에 대하여 각 위치로 이동이 가능한가? 확인
result = 0

for step in steps:
    next_row = row+ step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result+=1

print(result)