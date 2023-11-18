import sys
input = sys.stdin.readline
N, K = map(int,input().split())
L = list(map(int,input().split()))
i, j, cnt = 0, 0, 1
check, answer, jump = 0, 0, 0
while True:
	if i == N-1 or j == N-1:
		break
 
	if L[j] <= K:
		cnt += 1
		j += 1
	elif L[j] > K:
		if jump == 0:
			jump += 1
			cnt += 1
			check = j
			j += 1
		else:
			i = check + 1
			j = i
			answer = max(answer, cnt)
			cnt, check = 1, 0
			jump = 0
print(max(cnt, answer))