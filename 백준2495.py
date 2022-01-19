for i in range(3):
    s=input()
    #일단 연속해서 나오는 게 있는지 검증
    flag=False
    for i in range((len(s)-1)):
        if s[i]==s[i+1]:
            flag=True
            break
    D={}
    max=1
    t=-1
    
    sum=0
    #연속하는 게 있다. 이제 연속하는 숫자들의 개수를 나열해야 함
    for i in range(7):
        if i==6 and sum!=0 and s[7]==s[6]:
            sum+=1
            if sum>max:
                max=sum
        if s[i]==t: #이제 계속 비교를 하는데 t랑 숫자가 같아
            sum+=1    #그러면 sum을 하나씩 더해주기
            if sum>max:
                max=sum #만약에 max보다 커지면 바꿔주기
        if s[i+1]!=s[i] : #내 바로 뒤에꺼가 나랑 달라
            sum=0 #초기화해주고 내 뒤에껄로 가기
            continue
        elif sum==0: #내 뒤에꺼랑 같은데 sum은 0이었어
            t=s[i] #그 글자 특정해주기
            sum=1  #이제 시작해줘야 되니까 sum을 1로 시작해주기
            continue
    print(max)




            