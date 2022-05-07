

def solution(survey, choices):
    L=[0 for _ in range(27)]
    R=0; T=0; C=0; F=0; J=0; M=0; A=0; N=0;
    answer = ''
    for i in range(len(survey)):
        if choices[i]==1:
            L[ord(survey[i][0])-65]+=3
        elif choices[i]==2:
            L[ord(survey[i][0])-65]+=2
        elif choices[i]==3:
            L[ord(survey[i][0])-65]+=1
        elif choices[i]==5:
            L[ord(survey[i][1])-65]+=1
        elif choices[i]==6:
            L[ord(survey[i][1])-65]+=2
        elif choices[i]==7:
            L[ord(survey[i][1])-65]+=3
    if L[ord('R')-65]<L[ord('T')-65]:
        answer+='T'
    elif L[ord('R')-65]>=L[ord('T')-65]:
        answer+='R'
    if L[ord('C')-65]<L[ord('F')-65]:
        answer+='F'
    elif L[ord('C')-65]>=L[ord('F')-65]:
        answer+='C'
    if L[ord('J')-65]<L[ord('M')-65]:
        answer+='M'
    elif L[ord('J')-65]>=L[ord('M')-65]:
        answer+='J'
    if L[ord('A')-65]<L[ord('N')-65]:
        answer+='N'
    elif L[ord('A')-65]>=L[ord('N')-65]:
        answer+='A'
    return answer

print(solution(["TR", "RT", "TR"],[7,1,3]))

