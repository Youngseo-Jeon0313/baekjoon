'''
카카오 인턴 문제 5번과 유사.
근데 효율성 측면은 해결을 못했다ㅠㅠㅠ
문제 고루고루 풀어보고 효율성 높은 코드를 구경하자..!!
'''
import sys
input=sys.stdin.readline

N,M,R=map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
move = [[1,0],[0,1],[-1,0],[0,-1]]

def rotate():
    carr=[[] for _ in range(N)]
    for i in range(N): carr[i]=arr[i][:]
    sr=0; sc=0; er=N-1; ec=M-1;
    for depth in range(min(M,N)//2):
        r=sr; c=sc;
        for dx, dy in move:
            while True:
                nx=r+dx; ny=c+dy;
                if sr<=nx<=er and sc<=ny<=ec:
                    arr[nx][ny]=carr[r][c]
                    r=nx;c=ny
                else: break
        sr+=1; sc+=1; er-=1; ec-=1;

for r in range(R): rotate()

for i in range(N): print(*arr[i])