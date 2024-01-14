# 수학, 조합 + 브루트포스
from itertools import combinations as cb
from collections import defaultdict

def solution(dice):
    answer = []; max_ans = -float('inf')
    # 절반만 생각하겠다.
    List_cb = []
    for i in cb(range(len(dice)), len(dice)//2):
        List_cb.append(list(i))
    List_cb = List_cb[:len(List_cb)//2]
    #print(List_cb)

    def dfs(score_List, dict_temp, now_dice_num, num, probability):
        if now_dice_num == len(dice)//2:
            score_List[num] +=probability
            return 
        for i in dict_temp[now_dice_num]:
            dfs(score_List, dict_temp, now_dice_num+1, num+i, probability*dict_temp[now_dice_num][i])

    for m in List_cb:
        #나는 i에 들어있는 주사위들로 만들거고, 
        me = m
        #반대를 정하자
        you = []
        for j in range(len(dice)):
            if j not in me: you.append(j)
        #print(me, you)
        me_score = [0 for _ in range(501)]
        you_score = [0 for _ in range(501)]
        score_dict_me = [defaultdict(int) for _ in range(len(me))]
        score_dict_you = [defaultdict(int) for _ in range(len(you))]

        for i in range(len(me)):
            for j in range(6):
                score_dict_me[i][dice[me[i]][j]]+=1/6
        
        dfs(me_score, score_dict_me, 0, 0, 1)

        for i in range(len(you)):
            for j in range(6):
                score_dict_you[i][dice[you[i]][j]]+=1/6
        
        dfs(you_score, score_dict_you, 0, 0, 1)

        #print(me_score[:20])
        #print(you_score[:20])
        me_total_score = 0; you_total_score = 0; draw_score = 0
        for i in range(1,501):
            for j in range(1,501):
                if me_score[i] and you_score[j]:
                    if i<j:
                        you_total_score+=me_score[i]*you_score[j]
                    elif i>j:
                        me_total_score+=me_score[i]*you_score[j]
                  
        if me_total_score>max_ans:
            max_ans = me_total_score
            answer = m
        if you_total_score>max_ans:
            max_ans = you_total_score
            answer = you
        #print(m, me_total_score, draw_score, you_total_score)
        
            
    real_answer = []
    for i in answer:
        real_answer.append(i+1)
    
    return real_answer
