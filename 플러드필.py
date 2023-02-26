from collections import deque

def solution(n, m, image):
    # bfs 풀이 -> 큐를 인덱스에 넣어줘야겠다.
    answer = 0
    visited = [[False for _ in range(m)] for _ in range(n)]
    direction = [(0,1),(1,0),(-1,0),(0,-1)]
    
    for py in range(n):
        for px in range(m):
            if visited[py][px]:
                continue
                
            visited[py][px] = True
            Q = deque([(py,px)])
            cur_area = image[py][px]

            while Q:
                y,x = Q.popleft()
                    
                for d in direction:
                    ny = y + d[0]
                    nx = x + d[1]

                    if (0 <= ny < n and 0 <= nx < m) and not visited[ny][nx] and image[ny][nx] == cur_area:
                        visited[ny][nx] = True
                        Q.append((ny,nx))

            answer += 1

    return answer