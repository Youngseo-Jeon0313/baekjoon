import sys
sys.stdin.readline

def separate(x, k):
    if k == 1 or len(x) == 1:
        return sum(x)
    left = 1
    right = len(x) - 1
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        ls = separate(x[: mid], k - 1)
        rs = separate(x[mid :], k - 1)
        if ls < rs:
            left = mid + 1
            ans = ls
        elif ls > rs:
            right = mid - 1
            ans = rs
        else:
            ans = ls
            break
    
    return ans

input = sys.stdin.readline
N, K = map(int, input().split())
x = list(map(int, input().split()))

print(separate(x, K))
