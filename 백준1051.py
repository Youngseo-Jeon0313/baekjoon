
import sys
input=sys.stdin.readline


N,M=map(int, input().split())
L=list()
for i in range(N):
        L.append(list(input()))
        
max=0
j=0 #옆으로 가기 초기화
while j<M:
    i=0 #위아래로 가기 초기화
    while i<N:
        square=1 #만들 정사각형 초기화 
        while square<N-i and square<M-j: #자 일단 맨 처음 꼭짓점은 찍은 상태에서 만들수 있는 만큼 정사각형 만들자
            if L[i][j]==L[i][j+square] and L[i][j]==L[i+square][j+square] and L[i][j]==L[i+square][j]:
                if square>max:
                    max=square
            square+=1
        i+=1 #그 다음에 i를 하나씩 증가시킨다.
    j+=1 #옆으로 한 칸 가기

if max==0:
    print(1)
else:
    print((max+1)**2)