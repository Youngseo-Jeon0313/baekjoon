'''
D 라는 Dictionary를 만들고,
어떤 숫자가 나오면 바로 추가& +1하기
그 다음에 숫자가 만약에 지금껏 숫자와는 다르면 방금 내 꺼를 0으로 바꾸고
다음 index로 가서 +1 또 추가
근데 만약에 내가 또 나온다? 그러면 이제 아니다. 라고 출력

'''


t=int(input())
sum=t
for i in range(t):
    s=input()
    D={}
    s+='1'
    if len(s)==2:
        sum+=0
    else:
        flag=True
        for j in range(len(s)-1):
            if flag==False:
                break
            if s[j] in list(D.keys()):
                if D[s[j]]==0 or D[s[j]]==-100: #아니 완전 앞에서 이미 0으로 만들어줌
                    D[s[j]]=-100
                    print(1)
                else: #내 바로 앞에 있는 게 나랑 똑같았을 때
                    if s[j+1]!=s[j] and j!=len(s)-1:
                        D[s[j]]=0
                    D[s[j]]+=1 #다시 더해주기
                    
            else: #아직 없네 
                if s[j+1]!=s[j] and j!=len(s)-1: #근데 내 바로 뒤에 있는 게 나랑 달라
                        D[s[j]]=0 #일단 a:0으로 만들어주기
                else:
                    D[s[j]]=1 #일단 a:1로 만들어주기 
    print(D)
    if -100 in D.values():
        sum-=1

print(sum)