for _ in range(int(input())):
    n = int(input())
    print(f"Pairs for {n}:", end=' ')
    for i in range(1, n//2+1):
        if i != n-i:
            if i != 1:
                print(',', end=' ') #기준을 '앞'으로 생각한 구현
            print(i, n-i, end='')
    print()