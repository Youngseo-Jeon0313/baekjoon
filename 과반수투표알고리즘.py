#with stack

arr = [0] * 100
st = []

n = int(input())

for i in range(n):
    val = int(input())
    if not st:
        st.append(val)
    else:
        if st[-1] != val:
            st.pop()
        else:
            st.append(val)
    arr[i] = val

if not st:
    print("과반수 이상되는 수가 없습니다.")
else:
    # 실제 그 수가 과반수인지 한번 더 확인
    cnt = 0
    for i in range(n):
        if arr[i] == st[-1]:
            cnt += 1

    if cnt > n // 2:
        print("과반수 이상인 수 :", st[-1])
    else:
        print("과반수 이상되는 수가 없습니다.")

'''
3 1 2 2 1 1 1 1 2 1 3 2 1 1 1 2 에서 상쇄를 시켜나가보자.



3 1 2 2 1 1 1 1 2 1 3 2 1 1 1 2


2 2 1 1 1 1 2 1 3 2 1 1 1 2


2 2 1 1 1 1 2 1 3 2 1 1 1 2


2 1 1 1 2 1 3 2 1 1 1 2


1 1 2 1 3 2 1 1 1 2



1 1 3 2 1 1 1 2



1 2 1 1 1 2



1 1 1 2



1 1



'''