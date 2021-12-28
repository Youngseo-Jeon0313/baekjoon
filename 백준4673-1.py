n=39
ans=0
ddlist=[]
for i in range(len(str(n))):
    ddlist.append(str(n)[i])

for i in range(len(str(n))):
    ans+=int(ddlist[i])
ans+=n

#n이라는 숫자를 str으로 바꾼 후 잘라서 그 앞에 꺼.. 그리고 그 뒤에꺼 더한 다음에 원래 꺼도 더함

#이 문젠는 사실 n이 굉장히 큰 것까지 주어졌기 때문에 
#복잡도를 낮추어서 풀기 위해서 접근을 이런 식으로 하는 게 현명하다.