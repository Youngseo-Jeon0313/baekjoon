import copy

def solution(user_ids, banned_ids):
    banned_id_group_list = [[] for _ in range(len(banned_ids))]
    for banned_index in range(len(banned_ids)):
        for user_index in range(len(user_ids)):
            # ex. fr*do 와 
            banned_id = banned_ids[banned_index]
            user_id = user_ids[user_index]
            if len(banned_id)!=len(user_id): continue # 어차피 아님
            flag=True
            for index in range(len(banned_id)):
                if banned_id[index] == '*': continue
                if banned_id[index] != user_id[index]: flag=False; break
            if flag:
                banned_id_group_list[banned_index].append(user_index)
    # print(banned_id_group_list)
    candidate_list = []
    for group in banned_id_group_list:
        new_candidate_list = []
        if candidate_list:
            # 모든 원소를 다 꺼낸 후 
            for j in candidate_list:
                for i in group:
                    if i in j: continue
                    new_candidate_list.append(j+[i])
        else:
            for i in group:
                new_candidate_list.append([i])
        candidate_list = copy.deepcopy(new_candidate_list)
    result = []
    for candidate in candidate_list:
        candidate = sorted(candidate)
        if candidate not in result:
            result.append(candidate)
    return len(result)