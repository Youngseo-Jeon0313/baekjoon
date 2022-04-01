first=['r','R','s','e','E','f','a','q','Q','t','T','d','w','W','c','z','x','v','g']
second=['k','o','i','O','j','p','u','P','h','hk','ho','hl','y','n','nj','np','nl','b','m','ml','l']
last_possible=['r','s','f','q']
last_impossible=['R','rt','sw','sg','e','fr','fa','fq','ft','fx','fv','fg','a','qt','t','T','d','w','c','z','x','v','g']
sum=0
str=input()
letter=2
for i in range(len(str)-1):
    if letter==2 and str[i] in first: letter=1
    elif letter==1 : letter=2
    elif str[i] in last_possible: sum+=1; letter=1
    else: letter=1
print(sum)