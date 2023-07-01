import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n, k =map(int,input().split()) 
lines = []
for i in range(n):
    a, b = map(int, input().split())
    lines.append((a, b))
# 라인 스위핑 알고리즘 적용을 위한 선분의 시작점과 끝점 추출
events = []
for a, b in lines:
    events.append((a, 1))  # 시작점
    events.append((b, -1))  # 끝점
# 이벤트 포인트를 기준으로 정렬
events.sort()
# 라인 스위핑 알고리즘으로 가장 많이 중복되는 선분의 수 구하기
count = 0
max_count = 0
for x, e in events:
    count += e
    if count
print(max_count)

'''
4 2
10 70
20 50
50 90
65 95
'''

n = int(input())
lines = []
for i in range(n):
    a, b = map(int, input().split())
    lines.append((a, b))
# 라인 스위핑 알고리즘 적용을 위한 선분의 시작점과 끝점 추출
events = []
for a, b in lines:
    events.append((a, 1))  # 시작점
    events.append((b, -1))  # 끝점
# 이벤트 포인트를 기준으로 정렬
events.sort()
# 라인 스위핑 알고리즘으로 가장 많이 중복되는 선분의 수 구하기
count = 0
max_count = 0
for x, e in events:
    count += e
    max_count = max(max_count, count)
print(max_count)