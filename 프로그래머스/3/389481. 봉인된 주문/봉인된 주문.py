def solution(n, bans):
    # n = 24
    real_n = n
    bans_numList = []
    # 일단 삭제된 애들을 각각 숫자로 나타낸다.
    for ban in bans:
        # sum(26**자리수*char(알파벳-'a'+1))
        ban = ban[::-1]
        ban_num = 0
        for index in range(len(ban)):
            ban_num += 26**index*(ord(ban[index])-ord('a')+1)
        bans_numList.append(ban_num)
    bans_numList.sort()
    for i in bans_numList:
        if i<=real_n:
            real_n +=1
        else:
            break
    start = 11
    answer = ''
    print(real_n)    
    while real_n > 0:
        # 1을 더한 나머지로 알파벳을 구함
        real_n, remainder = divmod(real_n - 1, 26)
        answer=(chr(ord('a') + remainder))+answer  # 'a'부터 시작하여 문자로 변환
    return answer