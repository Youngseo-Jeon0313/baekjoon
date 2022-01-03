#탑다운 다이나믹 프로그래밍 소스코드
d = [0] * 100

def fibo(x):
    if x==1 or x==2:
        return 1
    if d[x] != 0: #이미 계산한 적 있는 문제라면 그대로 반환
        return d[x] #배열을 이용해서 계산한 적 있는 문제는 배열 안에다가 넣는 ,,
    d[x] = fibo(x-1) +fibo(x-2)
    return d[x]

print(fibo(99))

#bottom up  ------dp 이전에 계산된 결과를 일시적으로 기록해놓는다
d = [0] *100
d[1] =1
d[2] =1
n=99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])

#실제로 함수 호출을 해보면,,! 노드 끝까지 안가고도 해결 가능
