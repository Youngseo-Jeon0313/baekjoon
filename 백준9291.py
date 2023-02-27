import sys

input = sys.stdin.readline


def test(x, index):
    global prev
    i, j = index
    if len(list(set(x[i]))) == 9: # index가 속한 row에서 중복되는 수가 없으면
        X = [x[k][j] for k in range(9)]
        if len(list(set(X))) == 9: # index가 속한 column에서 중복되는 수가 없으면
            c = i // 3
            r = j // 3
            if (c, r) not in prev: # 3x3 영역을 처음 마주하면
                prev.append((c, r))
                C = x[i : i + 3]
                square = []
                for sq in C:
                    square += sq[j : j + 3]
                if len(list(set(square))) == 9: # index가 속한 3x3 영역에서 중복되는 수가 없으면
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    else:
        return False
    
T = int(input())
ans = []
for _ in range(T):
    prev = []
    array = []
    for i in range(9):
        array.append(list(map(int, input().split())))
    t = True
    for i in range(9):
        for j in range(9):
            if not test(array, (i, j)):
                t = False
                break
        if not t:
            break
    if not t:
        ans.append("INCORRECT")
    else:
        ans.append("CORRECT")
    if _ != T - 1:
        x = input()

for a in range(len(ans)):
    print(f"Case {a + 1}: {ans[a]}")