# 시간복잡도 - 100x100x8x5

N = int(input())
List = []
for _ in range(N):
    List.append(list(input()))

answer = 0
for i in range(N):
    for j in range(N):
        if List[i][j]=='M':
            # 위쪽 
            if i-4>=0 and List[i-1][j]=='O' and List[i-2][j]=='B' and List[i-3][j]=='I' and List[i-4][j]=='S':
                answer+=1
            # 아래쪽 
            if i+4<N and List[i+1][j]=='O' and List[i+2][j]=='B' and List[i+3][j]=='I' and List[i+4][j]=='S':
                answer+=1
            # 왼쪽 
            if j-4>=0 and List[i][j-1]=='O' and List[i][j-2]=='B' and List[i][j-3]=='I' and List[i][j-4]=='S':
                answer+=1
            # 오른쪽 
            if j+4<N and List[i][j+1]=='O' and List[i][j+2]=='B' and List[i][j+3]=='I' and List[i][j+4]=='S':
                answer+=1
            # 왼쪽 위 대각선 
            if i-4>=0 and j-4>=0 and List[i-1][j-1]=='O' and List[i-2][j-2]=='B' and List[i-3][j-3]=='I' and List[i-4][j-4]=='S':
                answer+=1
            # 오른쪽 아래 대각선
            if i+4<N and j+4<N and List[i+1][j+1]=='O' and List[i+2][j+2]=='B' and List[i+3][j+3]=='I' and List[i+4][j+4]=='S':
                answer+=1
            # 왼쪽 아래 대각선 
            if i+4<N and j-4>=0 and List[i+1][j-1]=='O' and List[i+2][j-2]=='B' and List[i+3][j-3]=='I' and List[i+4][j-4]=='S':
                answer+=1
            # 오른쪽 위 대각선 
            if i-4>=0 and j+4<N and List[i-1][j+1]=='O' and List[i-2][j+2]=='B' and List[i-3][j+3]=='I' and List[i-4][j+4]=='S':
                answer+=1

print(answer)

