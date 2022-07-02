C,L,leng=map(int,input().split())
str_arr=[]
road=[]
dic={}

for i in range(C):
    str_arr.append(input())
for i in range(C):
    for j in range(L):
            if str_arr[i][j] in dic.keys():
                dic[str_arr[i][j]].append([i,j])
            else:
                dic[str_arr[i][j]]=[[i,j]]
D,U,L,R=[1,0,0,0],[-1,0,0,0],[0,0,-1,0],[0,0,0,1]
charac=input()
def rec(x,y,ans,string):
    if str_arr[x][y]==ans:
        return
    else:
        rec(x+1,y,ans,string+'D')
        rec(x-1,y,ans,string+'U')
        rec(x,y+1,ans,string+'R')
        rec(x,y-1,ans,string+'L')

totalans=[];

sum=0;
before_x=0; before_y=0; flag=True;
charac=charac+'0'
while True:
    ans=[]
    for i in range(len(charac)):
        if charac[i]=='0':
            x,y=C-1,L-1
            if x>before_x: ans.append('D'*(x-before_x)); before_x=x
            if x<before_x: ans.append('U'*(before_x-x)); before_x=x;
            if y>before_y: ans.append('R'*(y-before_y)); before_y=y;
            if y<before_y: ans.append('L'*(before_y-y)); before_y=y;
        elif (charac[i] in dic.keys()) and len(list(dic[charac[i]]))>0  :
            x,y=dic[charac[i]].pop()
            before_x,before_y,ch,answer=rec(before_x,before_y,charac[i],'')
            ans.append(answer)
            ans.append('P')
        else: flag=False; break;
    if flag==False: break; 
    if flag==True: sum+=1; totalans.extend(ans)
ans=''
for i in totalans:
    ans+=i

print(sum, len(ans))
print(ans,sep='')