N, M=input().split()

N=int(N)
M=int(M)

t=int(input())
left=1
right=M
distance=0
for i in range(t):
    move=int(input())
    if left<=move and move <=right:
        continue
    if move<left:
        distance+=abs(move-left)
        left=move
        right=move+M-1
        
    else:
        distance+=abs(move-right)
        right=move
        left=move-M+1
        
print(distance)

'''
사과가 내 왼쪽에 있는지
오른쪽에 있는지
'''