import sys
input=sys.stdin.readline

N,R,C=map(int,input().split())
#정답을 저장해둘 배열
turn=0
def divide_and_conquer(x,y,size):
    global turn
    if y==R and x==C: 
        print(turn)
        exit()
    # print(x,y,size,turn)
    if size==1:
        turn+=1
        return
    if not (y<=R<y+size and x<=C<x+size):
        turn+=size*size
        return
    #4등분씩 방문. 기준은 맨 왼쪽 위
    else:    
        divide_and_conquer(x, y, size//2)
        divide_and_conquer(x+size//2, y,size//2)
        divide_and_conquer(x, y+size//2, size//2)
        divide_and_conquer(x+size//2,y+size//2, size//2)



divide_and_conquer(0, 0, 2**N)
