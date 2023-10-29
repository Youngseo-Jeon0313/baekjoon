'''
종치는 조건
1. 가장 위에 위치한 숫자 합이 5가 되는 순간 -> 수연
2. 숫자 5 나오는 순간! -> 도도

종치면?
내 덱
상대방 꺼 뒤집어서 그 밑에
내 그라운드에 있던 거 뒤집어서 그 밑에

승패
1. 내 덱에 있는 카드 수 0
2. M번 진행한 후 덱에 더 많은 카드 가진 사람
'''
from collections import deque
N, M = map(int,input().split())
dodo_deq = deque([])
suyeon_deq = deque([])

dodo_ground = deque([])
suyeon_ground = deque([])

for _ in range(N):
    dodo, suyeon = map(int,input().split())
    dodo_deq.append(dodo)
    suyeon_deq.append(suyeon)
    # 앞에 있을 수록 밑에 있는 거임 > 위를 꺼내려면 pop으로
turn = 0
for turn in range(M):
    # print("suyeon_deq",suyeon_deq)
    # print("suyeon_ground",suyeon_ground)
    # print("dodo_deq",dodo_deq)
    # print("dodo_ground",dodo_ground)
    

    if turn % 2 :
        present = suyeon_deq.pop()
        suyeon_ground.append(present)
    else:
        present = dodo_deq.pop()
        dodo_ground.append(present)

    if len(dodo_deq) ==0:
        print('su')
        exit()
    elif len(suyeon_deq) == 0:
        print('do')
        exit()

    if (present== 5):
        for j in suyeon_ground:
            dodo_deq.appendleft(j)
        for k in dodo_ground:
            dodo_deq.appendleft(k)
        # print('here!', dodo_deq,dodo_ground,suyeon_deq,suyeon_ground)
        suyeon_ground = deque([]); dodo_ground = deque([])
    
    elif suyeon_ground and dodo_ground and suyeon_ground[-1]+dodo_ground[-1] == 5:
        for j in dodo_ground:
            suyeon_deq.appendleft(j)
        for k in suyeon_ground:
            suyeon_deq.appendleft(k)
        suyeon_ground = deque([]); dodo_ground = deque([])
        

if len(dodo_deq) > len(suyeon_deq):
    print('do')
elif len(dodo_deq) == len(suyeon_deq):
    print('dosu')
else:
    print('su')
