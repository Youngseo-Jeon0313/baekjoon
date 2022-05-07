def solution(alp, cop, problems):
    answer = 0
    while problems:
        for i in range(len(problems)):
            #일단 얘네는 풀 수 가 있어야 함!
            if alp<=problems[i][0] and cop<problems[i][1]:
       #+그냥 알고력
       #+그냥 코딩력
    return answer


print(solution(10,10,[[10,15,2,1,2],[20,20,3,3,4]]))
print(solution(0,0,[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))
