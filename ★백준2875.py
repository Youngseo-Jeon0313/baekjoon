N,M,K= map(int, input().split())	# n 여학생 수, m 남학생 수, k 인턴쉽 학생 수
result = 0

while N>=2 and M>=1 and N+M>=K + 3:	# 2명 , 1명 팀 만들 수 있고, 인턴쉽도 보낼 수 있는 수 일때
    N-= 2	# 빼주고
    M-= 1	# 빼주고
    result += 1	# 팀 수는 하나씩 더해준다
print(result)

'''
직관, while문
'''