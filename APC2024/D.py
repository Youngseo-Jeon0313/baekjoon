N = int(input())
List = []
for _ in range(N):
    name, jaehaek_status, ICPC_win, shake_score, apc_score = input().split()
    List.append([name, jaehaek_status, ICPC_win, int(shake_score), int(apc_score)])
                
temp_answer = []
for i in List:
    if i[1] == 'jaehak' and i[2] == 'notyet' and (i[3]==-1 or i[3]>3):
        temp_answer.append([i[4], i[0]])


temp_answer.sort()
temp_answer = temp_answer[:10]
#print(len(temp_answer),temp_answer)

answer = []
for i in temp_answer:
    answer.append(i[1])
answer.sort()
print(len(answer))
for name in answer:
    print(name)

'''
25
kim jaehak winner 5 16
park jaehak notyet -1 18
choi hewhak winner 10 17
lee jaehak notyet 20 19
kimyu hewhak notyet 30 20
parkyu jaehak winner -1 15
choiyu hewhak notyet 1 14
leeyu jaehak notyet 9 12
baek jaehak notyet 8 11
shin jaehak notyet 4 13
han jaehak notyet 4 8
oh jaehak notyet 3 9
jang hewhak notyet -1 7
pang jaehak winner 2 10
jaegal jaehak notyet 14 6
sunwoo jaehak notyet 11 5
yang hewhak notyet -1 3
yoon jaehak winner 12 4
moon hewhak notyet -1 2
no hewhak winner 30 1
jeon jaehak notyet 8 20
young jaehak notyet 8 21
seo jaehak notyet 8 22
kim jaehak notyet 8 23
taehyun jaehak notyet 8 24
'''