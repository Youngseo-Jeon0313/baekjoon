# 세 수의 합
import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()

'''
x+y+z=k 라는 식을 x+y=k-z로 바꾸어 생각
'''

arr_sum = set()
for x in arr:
    for y in arr:
        arr_sum.add(x+y)


def check():
    global answer
    for i in range(N-1, -1, -1):
        for j in range(i+1):
            if arr[i]-arr[j] in arr_sum:
                answer = arr[i] #최대값을 찾게 되는 것
                return


answer = 0
check()
print(answer)