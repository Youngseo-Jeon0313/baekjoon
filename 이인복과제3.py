import itertools

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def is_inside_triangle(point, triangle):
    a = triangle[0]
    b = triangle[1]
    c = triangle[2]

    angle_sum = 0

    angle_sum += get_angle(point, a, b)
    angle_sum += get_angle(point, b, c)
    angle_sum += get_angle(point, c, a)

    return abs(angle_sum - 360) < 1e-9

def get_angle(point, a, b):
    vector1 = (a.x - point.x, a.y - point.y)
    vector2 = (b.x - point.x, b.y - point.y)

    cross_product = vector1[0] * vector2[1] - vector1[1] * vector2[0]
    dot_product = vector1[0] * vector2[0] + vector1[1] * vector2[1]

    angle = math.degrees(math.atan2(cross_product, dot_product))
    return angle if angle >= 0 else angle + 360

def get_polygon_points(points, selected_points):
    polygon_points = []

    for i in range(len(points)):
        if i in selected_points:
            polygon_points.append(points[i])

    return polygon_points

def count_white_points_inside(points, polygon_points):
    count = 0

    for point in points:
        if is_inside_polygon(point, polygon_points):
            count += 1

    return count

def is_inside_polygon(point, polygon_points):
    n = len(polygon_points)
    inside = False

    p1 = polygon_points[0]
    for i in range(1, n + 1):
        p2 = polygon_points[i % n]

        if point.y > min(p1.y, p2.y):
            if point.y <= max(p1.y, p2.y):
                if point.x <= max(p1.x, p2.x):
                    if p1.y != p2.y:
                        x_intersection = (point.y - p1.y) * (p2.x - p1.x) / (p2.y - p1.y) + p1.x
                        if p1.x == p2.x or point.x <= x_intersection:
                            inside = not inside

        p1 = p2

    return inside

def main():
    N, M = map(int, input().split())

    white_points = []
    for _ in range(M):
        x, y = map(int, input().split())
        white_points.append(Point(x, y))

    min_blue_points = float('inf')

    # 삼각형을 만들기 위해 적어도 3개의 점이 필요
    if M >= 3:
        for triangle_points in itertools.combinations(white_points, 3):
            outside_points = M - count_white_points_inside(white_points, triangle_points)

            if outside_points < min_blue_points:
                min_blue_points = outside_points

    print(min_blue_points)

if __name__ == "__main__":
    main()
