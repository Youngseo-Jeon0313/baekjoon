def solution(name):
    # name = "AAAB"
    answer = 0
    for i in name:
        answer += min(ord(i)-ord('A'), ord('Z')-ord(i)+1)

    temp=0
    shift=len(name)-1
    for i in range(len(name)):
        if name[i]=="A":
            temp=i
            while(temp<len(name) and name[temp]=="A"):
                temp+=1
            left=(0 if i==0 else i-1)
            right=len(name)-temp
            shift=min(shift,left+right+min(left,right))
    answer+=shift
    return answer