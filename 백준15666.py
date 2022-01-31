#중복순열로 푸는,,
#그리고 재귀함수로 푸는,,

def go(check, start):
    if sum(check) == m:
        ans = [arr[i] for i in range(n) if check[i]]
        print(' '.join(map(str,ans)))
        return
    for i in range(start, n): #check값에서 0인 값들 중에서 하나를 1로 바꾸어준다.
        if check[i] == 0:
            check[i] = 1
            go(check, i+1)
            check[i] = 0
             #나머지 하나도 0인 값을 또 하나 1로 바꾸어서 다시 고

n, m = map(int,input().split())
arr = sorted(list(map(int,input().split())))
go([0]*n, 0)