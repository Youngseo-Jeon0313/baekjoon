import sys
input = sys.stdin.readline

S = input()
T = input()


'''
S의 길이와 T의 길이가 50정도밖에 되지 않는다는 점이 매우 의심스럽습니다.
심지어 여기에서 시간을 2초나 준다는 것은... 
너무나도 브루트포스 향이 솔솔 납니다.
'''

def check(now):
    if now == S: return 1
    if len(now)<=len(S): return 0
    answer = 0
    
    if now[-1] == 'A':
        answer = check(now[:-1])
    
    if answer == 1: return 1
    if now[0] == 'B':
        temp = now[::-1]
        answer = check(temp[:-1])
    return answer

print(check(T))