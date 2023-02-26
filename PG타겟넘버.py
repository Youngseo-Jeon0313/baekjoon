
def backtracking(numbers, target, now_score, index):

    global check
    # print(check) 
    global answer
    if now_score==target:
        # print('hi', check)
        answer+=1
        return 
    for i in range(index, len(numbers)):
        if not check[i]:
            check[i]=1
            backtracking(numbers, target, now_score-numbers[i]*2, i+1)
            check[i]=0


def solution(numbers, target):
    global check
    global answer
    check=[0 for _ in range(len(numbers))]
    SUM=sum(numbers)
    answer = 0
    backtracking(numbers, target, SUM, 0)
    return answer

print(solution([1,1,1,1,1],3))
print(solution([4, 1, 2, 1],4))