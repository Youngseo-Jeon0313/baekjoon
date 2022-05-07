from collections import deque
move = [[0,1],[1,0],[0,-1],[-1,0]]
def Rotate(rc):
    copyarr=[[] for _ in range(len(rc))]
    for i in range(len(rc)):
        copyarr[i]=rc[i][:]
    row=0; column=0;
    for dx,dy in move:
        while True:
            nx=row+dx; ny=column+dy   
            if (row==0 or row==len(rc)-1 or column==0 or column==len(rc[0])-1) and 0<=nx<len(rc) and 0<=ny<len(rc[0]):
                rc[nx][ny]=copyarr[row][column]
                row=nx; column=ny
            else: break
    return rc
def ShiftRow(rc):
    copyarr=[[] for _ in range(len(rc))]
    for i in range(len(rc)):
            copyarr[i]=rc[i][:]
def solution(rc, operations):
    rc=deque(rc)
    for j in operations:
        if j=="ShiftRow":
            rc.appendleft(rc.pop())
        else:
            Rotate(rc)
    return (list(rc))

print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]],["Rotate", "ShiftRow"]))
print(solution([[8, 6, 3], [3, 3, 7], [8, 4, 9]],["Rotate", "ShiftRow", "ShiftRow"]))
print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],["ShiftRow", "Rotate", "ShiftRow", "Rotate"]))
