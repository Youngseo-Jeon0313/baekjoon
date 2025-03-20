def solution(citations):
    citations = sorted(citations)
    answer = 0
    for i in range(len(citations)):
        answer = max(answer,min(citations[i],len(citations)-i))
    return answer