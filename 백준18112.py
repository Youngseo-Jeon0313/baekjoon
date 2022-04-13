start=input()
end=input()

def dfs(num, sum):
    if num==int(end): return sum
    dfs(bin(int(num,2)+1),sum+1)
    dfs(bin(int(num,2)-1),sum+1)
    if int(num,2)!=0: 


sum=0
dfs(int(start), sum)