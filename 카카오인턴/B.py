# 수학, 조합 + 브루트포스
from itertools import combinations as cb

def solution(dice):
    # 절반만 생각하겠다.
    List_cb = []
    for i in cb(range(len(dice)), len(dice)//2):
        List_cb.append(list(i))
    List_cb = List_cb[:len(List_cb)//2]
    print(List_cb)

    for i in List_cb:
        #나는 i에 들어있는 주사위들로 만들거고, 
        me = i
        #반대를 정하자
        you = []
        for j in range(len(dice)):
            if j not in i: you.append(j)
        #print(me, you)
        me_score = [0 for _ in range(501)]
        you_score = [0 for _ in range(501)]
        

    answer = []
    
    return answer