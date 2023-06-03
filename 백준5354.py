t=int(input())
for i in range(t):
    n=int(input())
    print('#'*n)
    for _ in range(n-2):
        print('#'+'J'*(n-2)+'#')
    print('#'*n)
    if i<t-1:
        print()
    