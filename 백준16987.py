from copy import copy
'''
내구도가 작은 애를 먼저 조진다.
'''
N = int(input())
eggs = []
for i in range(N):
    a, b = map(int,input().split())
    eggs.append([i,a,b])

# 그냥 요구사항대로 똑같이 해.

# 가지고 칠 계란들 순서대로 
for i in range(N-1):
    if eggs[i][1]<=0: 
        continue
    #어떤 걸로 칠지 결정한다.
    temp_egg_list = eggs[:i].copy()+eggs[i+1::].copy()
    temp_egg_list = sorted(temp_egg_list, key=lambda x:[x[1]-x[2]])
    print('check',i,eggs,temp_egg_list)
    if temp_egg_list[0][1]<=0:
        continue
    
    eggs[i][1]-=temp_egg_list[0][2]
    eggs[temp_egg_list[0][0]][1]-=eggs[i][2]

answer=0

for j in range(N):
    if eggs[j][1]<=0:
        answer+=1
print(answer)