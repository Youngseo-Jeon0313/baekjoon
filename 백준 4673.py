#셀프 넘버
#숫자 자릿수 각각 더하기 방법 => list로 바꾼 후 더하면 됨!

def d(n):
    ans=0
    ddlist=[]
    for i in range(len(str(n))):
        ddlist.append(str(n)[i])

    for i in range(len(str(n))):
        ans+=int(ddlist[i])
    ans+=n
    return ans


    #셀프 넘버를 만드는 방법.! 1부터 쭉 그냥 계속해서 만들 수 있는 걸 무제한으로 만들어본다.
    #왜 set을 쓰는가?? list가 아니라? set은 중복이 안 되기 때문.
    #그리고 이 문제에서는 순서가 뒤죽박죽되더라도 sorted로 set을 오름차순으로 만들어줄 수 있다.


s_set = set()
for k in range(1,10001):
    s_set.add(d(k))
answer= set(range(1,10001))-s_set
for i in sorted(answer):
    print(i)