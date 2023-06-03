ans=[]
for j in range(5):
    s=input()
    for i in range(len(s)-2):
        # print( s[i:i+3])
        if s[i:i+3]=='FBI': ans.append(j+1)
if ans: 
    print(*set(ans))
else: print("HE GOT AWAY!")