'''
문제 설명은 어렵지만 그냥 문을 열고 닫고를 반복한 이후
상태를 묻는 문제
'''

for _ in range(int(input())):
    N = int(input())
    answer = 0
    rooms = [True for _ in range(N+1)]
    for i in range(1,N+1):
        check = i
        while check <= N:
            if rooms[check]:
                rooms[check] = False
            else:
                rooms[check] = True
            check += i
    for i in range(1,N+1):
        if not rooms[i]:
            answer += 1
    print(answer)