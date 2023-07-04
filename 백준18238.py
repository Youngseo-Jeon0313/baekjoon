S=input()
before='A'
ans=0
for i in S:
    a=ord(i)-ord(before)
    ans+=min(abs(a),26-abs(a))
    before=i
print(ans)