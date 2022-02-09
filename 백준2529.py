def go(idx):
    global minAns, maxAns
    if idx==n:
        val = ''.join(map(str,ans))
        if minAns[0] > int(val): minAns = [int(val),val]
        if maxAns[0] < int(val): maxAns = [int(val), val]
        return
    for i in range(10):
        if i not in ans:
            if (s[idx]=='<' and ans[-1]<i) or (s[idx]=='>' and ans[-1]> i):
                ans.append(i)
                go(idx+1)
                ans.pop()

n=int(input())
s=input().split()
ans=[]
minAns = [float('inf'), '']
maxAns = [0,'']
for i in range(10):
    ans.append(i)
    go(0)
    ans.pop()

print(maxAns[i])
print(minAns[i])