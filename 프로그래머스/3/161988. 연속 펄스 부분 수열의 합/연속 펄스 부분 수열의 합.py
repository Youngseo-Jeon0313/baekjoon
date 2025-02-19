def solution(sequence):
    answer = 0
    one = [-1,1]*(len(sequence)//2)+[-1]*(len(sequence)%2)
    two = [1,-1]*(len(sequence)//2)+[1]*(len(sequence)%2)
    one_sequence = []
    two_sequence = []
    for i in range(len(sequence)):
        one_sequence.append(sequence[i]*one[i])
        two_sequence.append(sequence[i]*two[i])
    # print(one_sequence)
    # print(two_sequence)
    # prefix_sum
    prefix_sum_one = [0 for _ in range(len(one_sequence)+1)]
    prefix_sum_two = [0 for _ in range(len(one_sequence)+1)]
    for i in range(1, len(prefix_sum_one)):
        prefix_sum_one[i]=prefix_sum_one[i-1]+one_sequence[i-1]
        prefix_sum_two[i]=prefix_sum_two[i-1]+two_sequence[i-1]
    min_value = 0;
    max_value = 0
    for i in range(1, len(prefix_sum_one)):
        min_value = min(min_value,prefix_sum_one[i])
        answer = max(answer, prefix_sum_one[i]-min_value)
    min_value = 0;
    max_value = 0
    for i in range(1, len(prefix_sum_two)):
        min_value = min(min_value,prefix_sum_two[i])
        answer = max(answer, prefix_sum_two[i]-min_value)
    return answer