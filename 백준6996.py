
'''
완전 잘못 생각했다ㅠㅠ

그냥 있는지만 판단하면 안 되고 아예 각각의 개수가 같냐 이것도 다 판단을 해야 함 ㅠ

1.dictionary로 낱말의 개수를 각각 넣어주고 (A), 이후에 B할 때는 하나씩 빼서 전부가 0이 되는지 판단하기
2.len이 같은지 비교하고 / sort를 통해 a,b,c.. 등을 나열시킨 후에 완전히 같은지 비교하기
'''

t=int(input())

for i in range(t):
    C,D=input().split()
    A=list(C)
    B=list(D)
    A.sort()
    B.sort()

    print(C,'&',D,'are',end=" ")
    if A==B:
        print('anagrams.')
    else:
        print('NOT anagrams.')


