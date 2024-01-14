N = int(input())
ans = [1]
target = 2
while len(ans)<=N:
    flag=True
    for i in ans:
        if (i*target)%(i+target)==0: 
            print(i,target)
            flag=False; break;
    if flag:
        ans.append(target)
    target+=1

print(*ans[:N])