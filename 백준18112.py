start=input()
end=input()

def dfs(num, sum):
    if int(num,2)==end: return sum
    dfs(bin(int(num,2)+1),sum+1)
    dfs(bin(int(num,2)-1),sum+1)
    if int(num,2)!=0: 
        for i in range(len(bin(num))):
            dfs(num^(1<<i),sum+1)

sum=0
dfs(start, sum)