arr = [int(input()) for _ in range(9)]
for a in range(9):
    for b in range(a+1, 9):
        for c in range(b+1,9):
            for d in range(c+1,9):
                for e in range(d+1,9):
                    for f in range(e+1,9):
                        for g in range(f+1,9):
                            length = arr[a] + arr[b] + arr[c] +arr[d] +arr[e] +arr[f] +arr[g]
                            if length == 100:
                                print(f'{arr[a]}\n{arr[b]}\n{arr[c]}\n{arr[d]}\n{arr[e]}\n{arr[f]}\n{arr[g]}')


'''
전체합에서 두 수를 빼서 100을 만드는 것도 좋다!
완전탐색으로 전체합에서 차례대로 하나씩 빼기

'''