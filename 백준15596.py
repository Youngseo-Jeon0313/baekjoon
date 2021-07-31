#정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.

#def solve(a: list) -> int
#a: 합을 구해야 하는 정수 n개가 저장되어 있는 리스트 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)

def solve(a) :
    x=0
    for i in a:
        x+=int(i)
    return(x)
