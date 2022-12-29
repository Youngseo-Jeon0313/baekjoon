dict={"I":1, "II":2, "IIV":3, "IV":4, "V":5, "VI":6, "VII":7, "IIX":8, "IX":9}

s=input()
index=0;
ans=0;
if s[0]=='X':
    while index<len(s):
        if s[index]=='X':            
            ans+=10
        else: break
        index+=1
if index<len(s):
    ans+=dict[s[index:len(s)]]

print(ans)