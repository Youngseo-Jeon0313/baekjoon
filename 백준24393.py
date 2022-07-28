import sys
input=sys.stdin.readline
from collections import deque


N=int(input())
card=deque([i for i in range(1,28)])
new_card_left=deque([])
new_card_right=deque([])
List=[]
for _ in range(N):
    # print(card)
    List=list(map(int,input().split()))
    for i in range(13):
        new_card_left.append(card.popleft())
    for i in range(14):
        new_card_right.append(card.popleft())
    
    # print('left',new_card_left)
    # print('right',new_card_right)
    for i in range(len(List)):
        store_list=[]
        if i%2==0: #홀수일 때
            for _ in range(List[i]):
                store_list.append(new_card_right.popleft())
            card.extend(store_list)
        else:
            for _ in range(List[i]):
                store_list.append(new_card_left.popleft())
            card.extend(store_list)

    # print('left',new_card_left)
    # print('right',new_card_right)
print(card.index(1)+1)