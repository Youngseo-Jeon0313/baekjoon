first_only=['E','Q','W']
second=['k','o','i','O','j','p','u','P','h','hk','ho','hl','y','n','nj','np','nl','b','m','ml','l']
last_possible=['r','s','f','q'] #다른 게 또 들어올 수 있는 애들 / 근데 안들어올 수도 있음
last_impossible_1=['R','e','a','t','T','d','w','c','z','x','v','g'] #종성 또는 초성으로 결정나는 애들
last_impossible_2=['rt','sw','sg','fr','fa','fq','ft','fx','fv','fg','qt',]
sum=0
str=input()
i=0
while i<=(len(str)-3):
    if (str[i] not in second) : i+=1; continue;
    if (str[i+1] in second): i+=1; continue;
    if str[i+1]==' ': i+=1
    elif str[i+1] in last_impossible_1: 
        if str[i+2]==' ': i+=1
        elif (str[i+2] not in second): i+=1  #종성
        else: sum+=1;  i+=1 #초성
    elif str[i+1] in last_possible:
        if str[i+2]==' ':i+=1
        elif str[i+2] in second and ((i+1==len(str)-2) or (str[i+3] not in first_only)): sum+=1; i+=1;
        elif i<len(str)-3 and str[i+2] not in second and str[i+3] in second and str[i+1:i+3] in last_impossible_2 and (i+3==len(str)-1 or str[i+4]!=' '): sum+=1; i+=1;
        else: i+=1
    else: i+=1

print(sum)