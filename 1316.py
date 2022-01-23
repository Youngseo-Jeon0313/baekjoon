'''
D 라는 Dictionary를 만들고,
어떤 숫자가 나오면 바로 추가& +1하기
그 다음에 숫자가 만약에 지금껏 숫자와는 다르면 방금 내 꺼를 0으로 바꾸고
다음 index로 가서 +1 또 추가
근데 만약에 내가 또 나온다? 그러면 이제 아니다. 라고 출력

'''


t=int(input())
sum=0

for i in range(t):
    s=input()
    L=[]
    flag=True
    if len(s)==2:
        sum+=0
    else:
        for i in range(len(s)):
            if s[i] not in L:
                L.append(s[i])
            else:
                if s[i]==L[-1]:
                    L.append(s[i])
                else:
                    flag=False
                    break
    if flag==True:
        sum+=1
print(sum)