def alphaToAscii(s):
    num= ord(s)
    ans=0
    while num>0:
        ans+=num%10
        num=num//10
    return ans
mystr=input()
for i in mystr:
    print(i*(alphaToAscii(i)))