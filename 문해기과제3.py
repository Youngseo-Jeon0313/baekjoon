import sys
input=sys.stdin.readline

def ccw(p1, p2, p3): #외적 -> 양수면 회전 방향 반시계 / 음수면 시계
    v1 = [p2[0] - p1[0], p2[1] - p1[1]]
    v2 = [p3[0] - p2[0], p3[1] - p2[1]]
    if v1[0] * v2[1] - v1[1] * v2[0] > 0: return True
    return False
     
'''
밧줄을 팽팽하게 해서 돌린다.
밧줄을 돌리는 조건? -> 우회전을 하면 잘못 왔다. 다시 가. until 첫번째 점

가장 최대의 볼록 다각형
'''
def convex_hull(dots):
    convex = []
    for p3 in dots:
        while len(convex) >= 2:
            # 가장 마지막에 넣은 두 점과 현재 넣으려는 점을 비교하여 ccw가 계속해서 반시계인지 확인 -> 아니면 convexhull에서 제외
            p1, p2 = convex[-2], convex[-1]
            if ccw(p1, p2, p3):
                break
            convex.pop()
        convex.append(p3)
    return len(convex)



N,M=map(int,input().split())
answer = 0; dots = []

# dots라는 배열 속에 (x,y) 좌표를 대입
for i in range(M):
    dots.append(list(map(int, input().split())))
     
# (x,y) 기준으로 정렬
dots = sorted(dots, key=lambda x:(x[0], x[1])) 
answer += convex_hull(dots)
 
#반시계로 정렬되었을 때 convex_hull 처리
dots.reverse()
answer += convex_hull(dots)

print(answer-2) # 시작점과 끝점을 중복으로 세는 현상으로 인해 -2 처리
"""
이 때 입력은 M이 3 이상이어야 하고, 셋 이상의 점이 한 직선 위에 있는 경우는 없다. 
"""