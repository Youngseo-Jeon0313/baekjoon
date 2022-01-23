'''
일단 구성이 맞는 수들을 다 정렬하고
그 다음에 가장 작은 거 꺼내오고,
그 다음에 그 숫자가 나보다 작으면 안 됨
'''

n=int(input())

#경우의 수는 n!
L=list(str(n))


k=0
for i in range(1,len(L)):
    if int(L[i])>int(str(n)[0]):
        print((L[i]),end='')
        L.pop(i)
        L.sort()
        print(''.join(L))
        break
    elif int(L[i])==int(str(n)[0]):
        if k!=0:
            print(str(n)[:i],end='')
            for j in range(i):
                L.pop(i)
            L.
    else:
        k+=1


if k==len(str(n))-1:
    print(0)