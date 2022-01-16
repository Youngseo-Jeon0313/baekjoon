arr = list(map(int,input().split()))
score = int(input())
arr = sorted(arr)

rank = 0
for i in range(len(arr)):
    if arr[i] == score: rank = len(arr) - i

if rank <= 5: print('A+')
elif rank <= 15: print('A0')
elif rank <= 30: print('B+')
elif rank <= 35: print('B0')
elif rank <= 45: print('C+')
elif rank <= 48: print('C0')
else:print('F')

'''
알고리즘을 잘 생각해야 함.
나는 이렇게 생각했음.
1등 1등 1등이 세 명 나오면 어떡하지?
근데 여기 문제에서 요구하는 건 어쨌든 한!사람의 등수만 요구하는 거니까 그냥 list로 만든 다음에 같은 사람이 있으면 
그 최소지점의 등수로 지정해주면 됨
'''