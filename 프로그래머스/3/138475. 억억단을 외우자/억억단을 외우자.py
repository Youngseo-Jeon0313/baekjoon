
def solution(e, starts):
    answer_list = [0 for _ in range(e+1)]
    for i in range(1, e+1):
        if i*i <= e:
	        answer_list[i*i]+=1
        for j in range(i+1, e + 1):
            n = i * j
            if n > e:
                break
            answer_list[n] += 2
    max_result = [0 for _ in range(e+1)]
    max_result[e] = e
    for i in range(e-1, min(starts)-1, -1): 
        if answer_list[i] >= answer_list[max_result[i+1]]:
            max_result[i] = i
        else:
            max_result[i] = max_result[i+1]

    return [max_result[s] for s in starts]
