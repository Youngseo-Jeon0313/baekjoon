s=input()
ans=0
List=[3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10]
for i in s:
    word=ord(i)-65
    ans+=(List[word])
    # print(ans)
print(ans)