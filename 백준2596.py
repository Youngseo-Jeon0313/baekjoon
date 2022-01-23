A=['0','0','0','0','0','0']
B=['0','0','1','1','1','1']
C=['0','1','0','0','1','1']
D=['0','1','1','1','0','0']
E=['1','0','0','1','1','0']
F=['1','0','1','0','0','1']
G=['1','1','0','1','0','1']
H=['1','1','1','0','1','0']

n=int(input())
M=list(input())
List=[]

for i in range(n):
    Mist=[]
    for j in range(6):
        Mist.append(M[6*i+j])
    List.append(int(''.join(Mist),2))
a=''
k=0
for i in range(n):
    if List[i]==0 or List[i]==1 or List[i]==2 or List[i]==4 or List[i]==8 or List[i]==16 or List[i]==32:
        a+=('A')
    elif List[i]==15 or List[i]==47 or List[i]==31 or List[i]==7 or List[i]==11 or List[i]==13 or List[i]==14:
        a+=("B")
    elif List[i]==19 or List[i]==51 or List[i]==3 or List[i]==27 or List[i]==23 or List[i]==17 or List[i]==18:
        a+=('C')
    elif List[i]==28 or List[i]==60 or List[i]==12 or List[i]==20 or List[i]==24 or List[i]==30 or List[i]==29:
        a+=("D")
    elif List[i]==38 or List[i]==6 or List[i]==54 or List[i]==46 or List[i]==34 or List[i]==36 or List[i]==39:
        a+=("E")
    elif List[i]==41 or List[i]==9 or List[i]==57 or List[i]==33 or List[i]==45 or List[i]==43 or List[i]==40:
        a+=("F")
    elif List[i]==53 or List[i]==21 or List[i]==37 or List[i]==61 or List[i]==49 or List[i]==55 or List[i]==52:
        a+=("G")
    elif List[i]==58 or List[i]==26 or List[i]==42 or List[i]==50 or List[i]==62 or List[i]==56 or List==59:
        a+=("H")
    else:
        print(i+1)
        k=1
        break

if k==0:
    print(a)
