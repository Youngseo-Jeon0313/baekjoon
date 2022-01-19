t=int(input())

for i in range(t):
    b=int(input()) #글자 개수 입력받기
    s=input() #글자 입력받기
    ans=[]
    for j in range(0, len(s), 8):
        x=list(s[j:j+8]) #8개를 기준으로 쪼개기
        for k in range(8): #그 8개를 확인하기
            if x[k] =='I': x[k]=1 #x라는 list에 I 또는 0 넣기
            else: x[k]=0
        x=''.join(map(str, x)) #x라는 list를 str으로 바꾸기
        x=int(x,2)  #int함수르리 이용해서 2진수를 10진수로 바꾸기
        ans.append(chr(x))
    print('Case #{}: {}'.format(i+1, ''.join(ans)))