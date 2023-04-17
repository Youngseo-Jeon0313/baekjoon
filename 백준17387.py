x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
p1 = [x1, y1]
p2 = [x2, y2]
p3 = [x3, y3]
p4 = [x4, y4]

#평행하면서, 두 선분이 하나의 직선에 있으면서 만나지 않는 상황 배제
if min(x1, x2) > max(x3, x4) or min(x3, x4) > max(x1, x2) or min(y1, y2) > max(y3, y4) or min(y3, y4) > max(y1, y2):
    print(0)
    quit()

def ccw(p1, p2, p3): #외적 -> 양수면 회전 방향 반시계 / 음수면 시계
    v1 = [p2[0] - p1[0], p2[1] - p1[1]]
    v2 = [p3[0] - p2[0], p3[1] - p2[1]]
    return v1[0] * v2[1] - v1[1] * v2[0]


a = ccw(p1, p2, p3) * ccw(p1, p2, p4)
b = ccw(p3, p4, p1) * ccw(p3, p4, p2)

if a <= 0 and b <= 0: #점 두 군데를 살펴보았을 때 모두 ccw가 +/-로 다른 방향으로 나왔다면 + 평행한데 일치
    print(1) #만난다.
else:
    print(0)