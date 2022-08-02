import sys
input=sys.stdin.readline

#List[끝나는수 0~9][몇자리수인지][비트마스크]=해당숫자 나열
List=[[[0 for _ in range(1024)] for _ in range(101)] for _ in range(10)]

#init
for i in range(1,10):
    List[i][1][1<<i]=1

#규칙에 맞는 점화식
#1,2,3,,,8까지의 숫자로 끝나는 경우에는 뒤에 두 개가 붙을 수 있으나 
#9로 끝나는 경우에는 뒤에 8만 붙을 수 있다.
#N-1로 끝나는 숫자들 중에서 가져와서 판단해서 넣고, 이 때 비트마스킹을 사용해서 0부터 9 중 뭘 썼는지 파악
for j in range(2,101):
    for k in range(10):
        for l in range(1024):
            if k==0: #1로 끝나는 애에서민 가져와야 한다.
                List[0][j][l|1<<(0)]+=(List[1][j-1][l])
            elif k==9: #8로 끝나는 애에서만 가져올 수 있다.
                List[9][j][l|1<<(9)]+=(List[8][j-1][l])
            else:
                List[k][j][l|1<<(k)]+=(List[k-1][j-1][l])
                List[k][j][l|1<<(k)] %=1000000000
            
                List[k][j][l|1<<(k)]+=(List[k+1][j-1][l])
                List[k][j][l|1<<(k)]  %=1000000000

N=int(input())
sum=0

for i in range(10):
    sum+=(List[i][N][1023]%1000000000) #N자리 수 중에서 / i로 끝나는 수 중 / 0부터 9 다 있는 수

print(sum%1000000000)