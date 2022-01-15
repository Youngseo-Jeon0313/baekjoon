T=int(input())
s,t=input().split('*')


for i in range(T):

    file=input()
    if file[0:len(s)]==s and file[-1:-len(t)-1:-1]==t[::-1] and (len(s)+len(t))<len(file):
        print('DA')
    else:
        print("NE")

#만족하지 않는 경우가 있는지 확인하자
#<=이거 조심