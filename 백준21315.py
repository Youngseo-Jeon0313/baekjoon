import sys
input= sys.stdin.readline
import math

'''
K+1 단계
i 단계에서는?
1 밑에서 2**k개의 카드를 맨 위로
2 직전에 맨 위로 올린 카드 중 2**(k-1)개의 카드를 맨 위로
3 직전에 맨 위로 올린 카드 중 2**(k-2)개의 카드를 맨 위로
4

..
K+1 2**0 개의 카드를 맨 위로

이 게임을 2번 한 결과를 보고
1번째 와 두 번째의 K가 무엇일까 ?? 를 맞추는 게임
'''

def game(cardList, k):
    result = []
    carry = cardList #뭐를 계속 가지고 다닌다.
    for i in range(k,-1,-1):
        #carry를 두 개로 쪼개서 하나는 붙이고 하나는 가지고 다닌다.
        result = carry[0:len(carry)-2**i] + result
        carry = carry[len(carry)-2**i:len(carry)]
        #print(k, carry)
    result = carry + result
    return result
N=int(input())
start = [str(i) for i in range(1,N+1)]
end = list(input().split())
max_K = math.ceil(math.log2(N))
for i in range(1,max_K):
    for j in range(1, max_K):
        one_game = game(start, i)
        two_game = game(one_game, j)
        #print(i, j, one_game, two_game)
        if two_game == end :
            print(i, j);
            exit();


'''
리스트 자를 때 index 오류 주의

'''

'''
테스트 케이스
3
1 2 3


'''