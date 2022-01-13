'''
b까지 i를 계속 진행시키는데 0부터 a-1까지는 continue로 건너뛰기
'''

a, b=map(int, input().split())
ans = 1
for i in range(b+1):
    if i<a: continue
    ans = (ans*(i*(i+1)//2)) %14579
print(ans)