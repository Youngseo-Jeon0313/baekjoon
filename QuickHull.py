def distance(p1, p2, p):
    # 점 p가 직선 p1p2에서의 거리를 계산하는 함수
    x1, y1 = p1
    x2, y2 = p2
    x, y = p
    return abs((y2 - y1) * x - (x2 - x1) * y + x2 * y1 - y2 * x1) / ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5

def find_hull(points, p1, p2, hull):
    # p1과 p2를 기준으로 Convex Hull을 찾는 재귀 함수
    if len(points) == 0:
        return

    farthest = None
    max_distance = 0

    for point in points:
        d = distance(p1, p2, point)
        if d > max_distance:
            farthest = point
            max_distance = d

    if farthest is None:
        return

    hull.append(farthest)
    points.remove(farthest)

    left_set = []
    right_set = []

    for point in points:
        if distance(p1, farthest, point) > 0:
            left_set.append(point)
        elif distance(farthest, p2, point) > 0:
            right_set.append(point)

    find_hull(left_set, p1, farthest, hull)
    find_hull(right_set, farthest, p2, hull)

def quick_hull(points):
    if len(points) < 3:
        return points

    hull = []
    min_x = min(points, key=lambda p: p[0])
    max_x = max(points, key=lambda p: p[0])

    hull.append(min_x)
    hull.append(max_x)

    points.remove(min_x)
    points.remove(max_x)

    left_set = []
    right_set = []

    for point in points:
        if distance(min_x, max_x, point) > 0:
            left_set.append(point)
        elif distance(max_x, min_x, point) > 0:
            right_set.append(point)

    find_hull(left_set, min_x, max_x, hull)
    find_hull(right_set, max_x, min_x, hull)

    return hull

# 예시 사용법
points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
convex_hull = quick_hull(points)
print(convex_hull)
